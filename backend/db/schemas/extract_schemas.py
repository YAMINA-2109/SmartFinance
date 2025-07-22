from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any

class FinancialExtractRequest(BaseModel):
    pdf_filename: Optional[str] = None

class FinancialUrlExtractRequest(BaseModel):
    url: HttpUrl

class FinancialExtractResponse(BaseModel):
    summary: str
    extracted_data: Dict[str, Any]
    download_csv_url: Optional[str] = None

