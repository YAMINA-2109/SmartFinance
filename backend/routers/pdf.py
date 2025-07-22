from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from db.schemas.pdf import PDFSummaryResponse, PDFQARequest, PDFQAResponse
from services import pdf_parser, summarizer, rag_qa
from pathlib import Path
import shutil
from db.database import SessionLocal
from db.models.chat_history import ChatHistory
import csv
from fastapi.responses import StreamingResponse
from io import StringIO
from sqlalchemy import text
from typing import Optional


router = APIRouter(prefix="/pdf", tags=["PDF"])

UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(exist_ok=True)

# Upload PDF
@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "PDF uploaded successfully", "filename": file.filename}

# Summarize PDF
@router.post("/summarize", response_model=PDFSummaryResponse)
async def summarize_pdf(file_name: str):
    file_path = UPLOAD_DIR / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="PDF file not found")

    text = pdf_parser.extract_text_from_pdf(file_path)
    summary = summarizer.summarize_text(text)

    return PDFSummaryResponse(filename=file_name, summary=summary)

# Ask Question about PDF

@router.post("/qa", summary="Ask Question")
async def qa_endpoint(request: PDFQARequest):
    try:
        result = rag_qa.ask_question(
            filename=request.filename,
            question=request.question,
            chat_history=request.chat_history
        )
        return {
            "answer": result["answer"],
            "sources": result["sources"]
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="PDF file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during QA: {str(e)}")


# Récupérer l’historique
@router.get("/history", summary="Get chat history")
def get_chat_history(filename: Optional[str] = Query(None)):
    db = SessionLocal()
    try:
        query = db.query(ChatHistory).order_by(ChatHistory.timestamp.desc())
        if filename:
            query = query.filter(ChatHistory.filename == filename)
        chats = query.all()
    finally:
        db.close()
    
    return [
        {
            "filename": chat.filename,
            "question": chat.question,
            "answer": chat.answer,
            "timestamp": chat.timestamp.isoformat()
        }
        for chat in chats
    ]

# Supprimer historique one ou all
@router.delete("/history", summary="Delete chat history")
def delete_chat_history(filename: Optional[str] = Query(None)):
    db = SessionLocal()
    try:
        query = db.query(ChatHistory)
        if filename:
            deleted = query.filter(ChatHistory.filename == filename).delete()
        else:
            deleted = query.delete()
        db.commit()
    finally:
        db.close()
    
    return {"message": f"{deleted} chat history entries deleted."}

# EXPORT all on CSV
@router.get("/history/export", summary="Export chat history as CSV")
def export_history_csv():
    db = SessionLocal()
    try:
        chats = db.query(ChatHistory).order_by(ChatHistory.timestamp.desc()).all()
    finally:
        db.close()

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(["filename", "question", "answer", "timestamp"])
    for chat in chats:
        writer.writerow([chat.filename, chat.question, chat.answer, chat.timestamp.isoformat()])

    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=chat_history.csv"
    })

# API Health Check
@router.get("/status", summary="API status check")
def status_check():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))
        db.close()
        return {"status": "ok", "message": "All systems operational"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Status check failed: {str(e)}")


# Extract raw text from PDF without ai or any 
@router.get("/extract", summary="Extract raw text from PDF")
def extract_pdf(file_name: str = Query(..., description="Name of the uploaded PDF file")):
    file_path = UPLOAD_DIR / file_name
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="PDF not found")

    text = pdf_parser.extract_text_from_pdf(file_path)
    return {"filename": file_name, "content": text}

