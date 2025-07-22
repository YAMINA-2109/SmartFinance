from pathlib import Path
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path: Path) -> str:
    try:
        reader = PdfReader(str(file_path))
        text = ""

        for page in reader.pages:
            text += page.extract_text() or ""

        if not text.strip():
            raise ValueError("No text found in PDF.")

        return text.strip()

    except Exception as e:
        raise RuntimeError(f"Error while reading PDF: {str(e)}")
