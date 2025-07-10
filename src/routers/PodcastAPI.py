
from src.services import extract_text_from_pdf, generate_audio
from llm_services.pdf_summarizer.summarizer import summarize_text
from src.utils.common import (
    temp_path_generator,
    file_generator,
    base64_converter
)


from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse
import aiofiles
import os
from typing import Optional
from uuid import uuid4
import base64

router = APIRouter()

@router.post("/podcast-summary", summary="Upload PDF and generate podcast")
async def upload_pdf(
    file: UploadFile = File(...),
    password: Optional[str] = Form(None)  # Optional password from form
):
    temp_path = f"temp_{uuid4()}_{file.filename}"
    temp_path = temp_path_generator(temp_path)

    await file_generator(temp_path, file)

    try:
        # Extract text with optional password
        raw_text, message = extract_text_from_pdf(temp_path, password=password or "")

        if not raw_text:
            os.remove(temp_path)
            raise HTTPException(status_code=400, detail=message)

        # Generate summary and audio
        summary = summarize_text(raw_text)

        audio_path, audio_file_name = generate_audio(summary)


        base64_data = await base64_converter(temp_path)


        os.remove(temp_path)

        

        return {
            "message": message,
            "transcript": summary,
            # "audio_url": audio_path,
            "audio_file_name": audio_file_name,
            "audio_base64":base64_data
        }

    except Exception as e:
        os.remove(temp_path)
        raise HTTPException(status_code=500, detail=str(e))
    





@router.get("/audio/{file_name}")
async def get_audio(file_name:str):
    file_path = os.path.join("src","outputs", file_name)

    
    if not os.path.exists(file_path):
        return {"error": "File not found"}

    return FileResponse(
        path=file_path,
        media_type="audio/mp3",
        filename=file_name
    )





