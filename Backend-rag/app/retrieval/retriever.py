import os
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_classic.retrievers.document_compressors.chain_extract import LLMChainExtractor

from app.core.embeddings import get_embeddings
from app.core.llm import get_llm
from app.core.config import FAISS_INDEX_PATH

def get_retriever():
    if not os.path.exists(FAISS_INDEX_PATH):
        raise RuntimeError(
            "FAISS index not found. Upload documents before querying."
        )
    embeddings = get_embeddings()
    llm = get_llm()

    vectorstore = FAISS.load_local(
        FAISS_INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    base_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    compressor = LLMChainExtractor.from_llm(llm)

    return ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
    )

