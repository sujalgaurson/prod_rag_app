import os
from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
GROQ_API_KEY= os.getenv("GROQ_API_KEY")
FAISS_INDEX_PATH = "data/faiss_index"

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")