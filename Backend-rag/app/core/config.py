import os
from dotenv import load_dotenv

load_dotenv()

TESTING = os.getenv("TESTING", "false").lower() == "true"

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 
GROQ_API_KEY= os.getenv("GROQ_API_KEY")
FAISS_INDEX_PATH = "data/faiss_index"

if not TESTING and not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")