import os
import shutil
from app.core.config import FAISS_INDEX_PATH

def delete_faiss_index():
    if os.path.exists(FAISS_INDEX_PATH):
        shutil.rmtree(FAISS_INDEX_PATH)
