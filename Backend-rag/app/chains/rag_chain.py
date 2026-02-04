from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from app.chains.query_rewriter import build_query_rewriter
from app.retrieval.hybrid_retriever import get_hybrid_retriever

from app.core.llm import get_llm
from app.retrieval.retriever import get_retriever

def build_rag_chain():
    llm = get_llm()
    retriever = get_retriever()
    hybrid_retrieve = get_hybrid_retriever()
    rewriter = build_query_rewriter()  # this is to rewrite vague queries

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant. Answer the question using ONLY the context below.
If you don't know the answer, say you don't know.

Context:
{context}

Question:
{question}

Answer:
""")

    def format_docs(docs):
        return "\n\n".join(d.page_content for d in docs)

    chain = (
        rewriter
        | RunnableLambda(
            lambda rewritten_question: {
                "question": rewritten_question,
                "context": format_docs(
                    hybrid_retrieve(rewritten_question)
                )
            }
        )
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
