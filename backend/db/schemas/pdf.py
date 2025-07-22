from pydantic import BaseModel
from typing import List, Tuple

# Summary Response 
class PDFSummaryResponse(BaseModel):
    filename: str
    summary: str

# QA Request
class PDFQARequest(BaseModel):
    question: str
    filename: str
    chat_history: List[Tuple[str, str]]

# QA Response
class PDFQAResponse(BaseModel):
    answer: str
    sources: List[str]
