from rank_bm25 import BM25Okapi
from langchain_core.documents import Document
import pickle
import os

BM25_PATH = "data/bm25.pkl"

class BM25Retriever:
    def __init__(self, documents):
        self.documents = documents
        self.corpus = [doc.page_content.split() for doc in documents]
        self.bm25 = BM25Okapi(self.corpus)

    def get_relevant_documents(self, query: str, k: int = 5):
        scores = self.bm25.get_scores(query.split())
        ranked_docs = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True
        )
        return [doc for doc, _ in ranked_docs[:k]]

    def save(self):
        with open(BM25_PATH, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load():
        with open(BM25_PATH, "rb") as f:
            return pickle.load(f)
