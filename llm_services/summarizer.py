import openai

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from src.app_core.app_settings import OPENAI_API_KEY
from llm_services.summarizer_prompt import summary_template 

# openai.api_key = OPENAI_API_KEY

def summarize_text(text: str) -> str:
        
    summary_template_prompt = PromptTemplate(
        input_variables=["information"], 
        template=summary_template
        )
    
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini") 
    chain = summary_template_prompt | llm 

    result = chain.invoke(input={"information":text})

    return result.content