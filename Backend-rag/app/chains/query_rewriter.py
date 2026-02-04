from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.core.llm import get_llm

def build_query_rewriter():
    """
    Returns a chain that rewrites vague questions into
    a context-aware, retrieval-friendly query.
    """
    llm = get_llm()

    # Prompt template to rewrite questions
    prompt = ChatPromptTemplate.from_template("""
        You are a query rewriting assistant.
        Rewrite the user's question to be clear, specific, and retrieval-friendly,
        without adding any information not present in the question.
        
        User Question:
        {question}
        
        Rewritten Query:
        """)

    # Runnable chain: input -> prompt -> LLM -> output string
    chain = {
        "question": RunnablePassthrough()
    } | prompt | llm | StrOutputParser()

    return chain
