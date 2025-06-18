from fastapi import APIRouter, UploadFile, File
from src.services import extract_text_from_pdf, generate_audio
from llm_services import summarize_text
import aiofiles
import os

router = APIRouter()

@router.post("/", summary="Upload PDF and generate podcast")
async def upload_pdf(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"
    async with aiofiles.open(temp_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    raw_text = extract_text_from_pdf(temp_path)
    summary = summarize_text(raw_text)
    audio_path = generate_audio(summary)

    os.remove(temp_path)

    return {
        "transcript": summary,
        "audio_url": audio_path
    }
