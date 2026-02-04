from app.retrieval.bm25_retriever import BM25Retriever
from app.retrieval.retriever import get_retriever as get_faiss_retriever

def get_hybrid_retriever(k: int = 5):
    faiss_retriever = get_faiss_retriever()  # ContextualCompressionRetriever
    bm25 = BM25Retriever.load()

    def retrieve(query: str):
        # ✅ LCEL-compatible call
        faiss_docs = faiss_retriever.invoke(query)
        bm25_docs = bm25.get_relevant_documents(query, k=k)

        # Merge + deduplicate
        unique_docs = {}
        for doc in faiss_docs + bm25_docs:
            unique_docs[doc.page_content] = doc

        return list(unique_docs.values())[:k]

    return retrieve
