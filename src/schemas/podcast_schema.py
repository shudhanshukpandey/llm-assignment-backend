from pydantic import BaseModel, Field

class PDFUploadResponse(BaseModel):
    transcript: str
    audio_url: str

class PDFUploadInput(BaseModel):
    pdf_url: str = Field(..., example="https://arxiv.org/pdf/1706.03762.pdf")
