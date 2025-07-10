
from src.app_core.app_settings import OPENAI_API_KEY


from langchain_community.document_loaders import PyPDFLoader

async def file_loader(file_path):
    loader = PyPDFLoader(file_path)
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)
   
    return pages