
import os
from uuid import uuid4
from fastapi import (
    APIRouter,
    File,
    UploadFile
)

from src.services.process_pdf_service import (
    process_pdf,
    get_response
)

from ..schemas.input_payload_schema import QuestionSchema

router = APIRouter()

@router.post("/upload-file", summary="API to read pdf file provoded by the user")
async def read_pdf(file:UploadFile=File(...)):
    try:
        thread_id = uuid4()
        await process_pdf(file, thread_id)

        return {"staus":True,"message":"file processed, Please use thread_id to ask questions","thread_id":thread_id}
    except Exception as err:
        return {"status":False,"message":f"error occured during processing pdf, {str(err)}"}


@router.post("/ask-question/{thread_id}", summary="API to Ask question from already provided pdf file")
async def ask_ques(question:QuestionSchema, thread_id:str):
    try:
        response_data = await get_response(question, thread_id)
        return response_data
    except Exception as err:
        return {"staus":False,"message":f"error occured during fetching response {str(err)}"}


