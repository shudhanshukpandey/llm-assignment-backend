from src.app_core.app_settings import *
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI, OpenAI


from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from .prompts import RETRIEVER_CHAT_PROMPT

def embed_data(pages, db_path):

    vector_store = FAISS.from_documents(pages, OpenAIEmbeddings())
    vector_store.save_local(db_path)

    return

def retrieve_data(question, db_path):
    vector_db = FAISS.load_local(db_path, OpenAIEmbeddings(), allow_dangerous_deserialization=True)

    # retriever = vector_db.as_retriever(search_type='mmr')
    # answer = retriever.invoke(question) #will give raw data as response

    combine_docs_chain = create_stuff_documents_chain(
        OpenAI(), RETRIEVER_CHAT_PROMPT

    )

    retrival_chain = create_retrieval_chain(
        vector_db.as_retriever(search_kwargs= {"k":3}), combine_docs_chain
    )

    answer = retrival_chain.invoke({"input":question})

    return answer



