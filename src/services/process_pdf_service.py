
import os
import shutil
from src.utils.common import file_generator, temp_path_generator, base64_converter
from llm_services.pdf_rag.file_content_extractor import file_loader
from llm_services.pdf_rag.file_vcrud import embed_data, retrieve_data

from .text_to_audio import generate_audio

async def process_pdf(file, thread_id):

    file_path = temp_path_generator(file.filename, "src", "temp")
    await file_generator(file_path, file)
    pages = await file_loader(file_path)
    os.remove(file_path)

    vector_db_path = temp_path_generator(str(thread_id),"llm_services","local_vector_db")

    embed_data(pages, vector_db_path)

    return {
        "staus":True,
        "message":"data has been processed and stored"
    }
   
async def get_response(question, thread_id):

   
    vector_db_path = temp_path_generator(str(thread_id),"llm_services","local_vector_db")
    response = retrieve_data(question.question, vector_db_path)


    audio_file_path, auddio_file_name = generate_audio(response.get('answer'))

    base64_data = await base64_converter(audio_file_path)
    os.remove(audio_file_path)
   
    return {"status":True,
            "answer":response.get('answer'), 
            "context":response.get("context"),
            "audio_base64":base64_data
            
            }


   




