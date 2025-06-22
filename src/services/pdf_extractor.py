from PyPDF2 import PdfReader
from typing import Tuple

def extract_text_from_pdf(pdf_path: str, password: str = "") -> Tuple[str, str]:
    try:
        reader = PdfReader(pdf_path)
        
        # Check for encrypted PDF
        if reader.is_encrypted:
            if password:
                try:
                    reader.decrypt(password)
                except Exception as e:
                    return "", f"Failed to decrypt PDF: {e}"
            else:
                return "", "PDF is password protected. Please provide a password."

        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

        if not text.strip():
            return "", "PDF contains no extractable text."
        
        return text, "Text extraction successful."

    except Exception as e:
        return "", f"An error occurred while reading the PDF: {e}"
