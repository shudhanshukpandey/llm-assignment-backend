
from src.services import extract_text_from_pdf, generate_audio
from llm_services import summarize_text


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

        audio_path, audio_file_name = generate_audio(summary)

        with open(audio_path, "rb") as audio_file:
            audio_base64 = base64.b64encode(audio_file.read()).decode("utf-8")


        os.remove(temp_path)

        

        return {
            "message": message,
            "transcript": summary,
            # "audio_url": audio_path,
            "audio_file_name": audio_file_name,
            "audio_base64":audio_base64
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





