
from src.services import extract_text_from_pdf, generate_audio
from llm_services import summarize_text


from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse
import aiofiles
import os
from typing import Optional
from uuid import uuid4

router = APIRouter()

@router.post("/podcast-summary", summary="Upload PDF and generate podcast")
async def upload_pdf(
    file: UploadFile = File(...),
    password: Optional[str] = Form(None)  # Optional password from form
):
    temp_path = f"temp_{uuid4()}_{file.filename}"

    # Save uploaded file temporarily
    async with aiofiles.open(temp_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    try:
        # Extract text with optional password
        raw_text, message = extract_text_from_pdf(temp_path, password=password or "")

        if not raw_text:
            os.remove(temp_path)
            raise HTTPException(status_code=400, detail=message)

        # Generate summary and audio
        summary = summarize_text(raw_text)

        audio_path = generate_audio(summary)

        os.remove(temp_path)

        

        return {
            "message": message,
            "transcript": summary,
            "audio_url": audio_path
        }

    except Exception as e:
        os.remove(temp_path)
        raise HTTPException(status_code=500, detail=str(e))
    







