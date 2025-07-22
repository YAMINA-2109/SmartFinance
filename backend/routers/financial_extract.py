from fastapi import APIRouter, HTTPException
from db.schemas.extract_schemas import (
    FinancialExtractRequest,
    FinancialUrlExtractRequest,
    FinancialExtractResponse
)
from services.rag_financial_service import (
    extract_financial_info_from_pdf,
    extract_financial_info_from_url
)
from fastapi.responses import StreamingResponse
from io import StringIO
import csv


router = APIRouter(prefix="/finance", tags=["Finance"])

@router.post("/extract-financial-info-from-pdf", response_model=FinancialExtractResponse)
def extract_financial_info_from_pdf_route(payload: FinancialExtractRequest):
    try:
        return extract_financial_info_from_pdf(payload.pdf_filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/extract-financial-info-from-url", response_model=FinancialExtractResponse)
def extract_financial_info_from_url_route(payload: FinancialUrlExtractRequest):
    try:
        return extract_financial_info_from_url(payload.url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/export-csv", summary="Export last financial data as flattened CSV")
def export_flat_csv():
    from pathlib import Path
    from utils.langchain_rag import query_rag_chain_details
    from utils.langchain_loader import load_pdf

    file_path = Path("uploaded_files/pdf_example_reporte.pdf")
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="No file found.")

    text = load_pdf(str(file_path))
    summary, data = query_rag_chain_details(text)

    def flatten_dict(d, parent_key='', sep='_'):
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    flat_data = flatten_dict(data)

    # Génération du CSV en mémoire
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=flat_data.keys())
    writer.writeheader()
    writer.writerow(flat_data)
    output.seek(0)

    return StreamingResponse(output, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=financial_data_flat.csv"
    })
