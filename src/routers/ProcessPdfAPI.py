
import os
from uuid import uuid4
from typing import List

from src.app_core.db import get_db
from sqlalchemy.orm import Session
from fastapi import (
    APIRouter,
    File,
    UploadFile,
    Depends
)

from src.services.process_pdf_service import (
    process_pdf,
    get_response
)

from ..schemas.input_payload_schema import QuestionSchema
from ..schemas.file_mapping_schema import FileMappingSchema
from ..models.file_maping import FileMapping

router = APIRouter()

# @router.post("/upload-file", summary="API to read pdf file provoded by the user")
# async def read_pdf(file:UploadFile=File(...)):
#     try:
#         thread_id = uuid4()
#         await process_pdf(file, thread_id)

#         return {"staus":True,"message":"file processed, Please use thread_id to ask questions","thread_id":thread_id}
#     except Exception as err:
#         return {"status":False,"message":f"error occured during processing pdf, {str(err)}"}

@router.post("/upload-file", summary="API to read PDF file provided by the user")
async def read_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        # Check for duplicate file_name
        existing = db.query(FileMapping).filter_by(file_name=file.filename).first()
        if existing:
            return {
                "status": False,
                "message": f"A file with name '{file.filename}' already exists. Use a different name."
            }

        # Generate new UUID and process
        thread_id = str(uuid4())
        await process_pdf(file, thread_id)

        # Store mapping in DB
        mapping = FileMapping(uuid=thread_id, file_name=file.filename)
        db.add(mapping)
        db.commit()

        return {
            "status": True,
            "message": "File processed. Please use thread_id to ask questions.",
            "thread_id": thread_id
        }

    except Exception as err:
        return {
            "status": False,
            "message": f"Error occurred during PDF processing: {str(err)}"
        }



@router.post("/ask-question/{thread_id}", summary="API to Ask question from already provided pdf file")
async def ask_ques(question:QuestionSchema, thread_id:str):
    try:
        response_data = await get_response(question, thread_id)
        return response_data
    except Exception as err:
        return {"staus":False,"message":f"error occured during fetching response {str(err)}"}


@router.get("/file-mappings", response_model=List[FileMappingSchema])
def get_mappings(db: Session = Depends(get_db)):
    return db.query(FileMapping).all()


@router.delete("/mappings/clear", summary="Delete all file mapping records")
def clear_file_mappings(db: Session = Depends(get_db)):
    try:
        deleted = db.query(FileMapping).delete()
        db.commit()
        return {
            "status": True,
            "message": f"{deleted} records deleted from file_mappings."
        }
    except Exception as err:
        db.rollback()
        return {
            "status": False,
            "message": f"Error occurred while deleting records: {str(err)}"
        }