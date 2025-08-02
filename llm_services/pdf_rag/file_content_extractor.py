
from src.app_core.app_settings import OPENAI_API_KEY


from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

async def file_loader(file_path):
    loader = PyPDFLoader(file_path)

    loader = PyPDFLoader(file_path)
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = splitter.split_documents(documents)
   
    return docs