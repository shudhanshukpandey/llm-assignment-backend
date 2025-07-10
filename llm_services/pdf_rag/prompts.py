from src.app_core.app_settings import *
from langchain import hub

RETRIEVER_CHAT_PROMPT = hub.pull("langchain-ai/retrieval-qa-chat")

