from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from app.core.config import GROQ_API_KEY
from langchain_core.language_models.fake import FakeListLLM
import os

def get_llm():

    if os.getenv("TESTING") == "true":
      return FakeListLLM(
          responses=["LangChain is a framework for building RAG systems."]
      )
    
    # return ChatOpenAI(
    #     model="gpt-4o-mini",
    #     temperature=0
    # )
    
    return ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY,
        temperature=0
    )

