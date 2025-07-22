import csv
from pathlib import Path
from db.schemas.extract_schemas import FinancialExtractResponse
from utils.langchain_loader import load_pdf, load_web
from utils.langchain_rag import query_rag_chain_details

def extract_financial_info_from_pdf(filename: str) -> FinancialExtractResponse:
    pdf_path = Path("uploaded_files") / filename
    if not pdf_path.exists():
        raise FileNotFoundError(f"File path {pdf_path} is not a valid file.")

    text = load_pdf(str(pdf_path))
    summary, fields = query_rag_chain_details(text)

    csv_path = Path("downloads") / f"{filename}_financial_data.csv"
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    with open(csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Field", "Value"])
        for key, val in fields.items():
            writer.writerow([key, val])

    return FinancialExtractResponse(
        summary=summary,
        extracted_data=fields,
        download_csv_url=f"http://localhost:8000/downloads/{csv_path.name}"
    )

def extract_financial_info_from_url(url: str) -> FinancialExtractResponse:
    text = load_web(url)
    summary, fields = query_rag_chain_details(text)

    return FinancialExtractResponse(
        summary=summary,
        extracted_data=fields,
        download_csv_url=None
    )
