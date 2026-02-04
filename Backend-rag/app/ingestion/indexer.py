import os
from langchain_community.vectorstores import FAISS
from app.core.embeddings import get_embeddings
from app.core.config import FAISS_INDEX_PATH
from app.retrieval.bm25_retriever import BM25Retriever

def create_or_update_index(chunks):
    embeddings = get_embeddings()

    if os.path.exists(os.path.join(FAISS_INDEX_PATH, "index.faiss")):
        # Load existing index
        db = FAISS.load_local(
            FAISS_INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )
        db.add_documents(chunks)
    else:
        # Create new index
        db = FAISS.from_documents(chunks, embeddings)

    db.save_local(FAISS_INDEX_PATH)

    # BM25
    bm25 = BM25Retriever(chunks)
    bm25.save()