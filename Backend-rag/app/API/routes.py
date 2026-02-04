from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil

from app.ingestion.loaders import load_document
from app.ingestion.splitter import split_documents
from app.ingestion.indexer import create_or_update_index
from app.chains.rag_chain import build_rag_chain
from app.EVALUATION.ragas_eval import evaluate_answer 
from app.utils.cleanup import delete_faiss_index

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the RAG API"}

@router.delete("/session/end")
def end_session():
    delete_faiss_index()
    return {"status": "FAISS index deleted"}

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    file_path = f"data/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    docs = load_document(file_path)
    chunks = split_documents(docs)
    create_or_update_index(chunks)

    return {"status": "Document indexed successfully"}

@router.post("/query")
def query_rag(question: str):
    try:
        rag_chain = build_rag_chain()
        answer = rag_chain.invoke(question) #generate answers

        # Get documents used for context (assuming hybrid_retrieve or retriever)
        # Adjust this depending on how you return docs from your RAG chain
        # from app.retrieval.hybrid_retriever import get_hybrid_retriever
        # docs = get_hybrid_retriever().invoke(question)
        # context_docs = [d.page_content for d in docs]

        # Evaluate answer with RAGAS
        # evaluation = evaluate_answer(question, answer, context_docs)

        return {"answer": answer}
    except RuntimeError as e:
        raise HTTPException(status_code=400, detail=str(e))
