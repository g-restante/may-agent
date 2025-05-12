from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from typing import Optional
from settings import settings 
import os
import logging

# Configurazione del logger
logger = logging.getLogger(__name__)

# Configurazione parametrizzata
EMBEDDING_MODEL = settings.embedding_model
LLM_MODEL = settings.llm_model
DB_LOCATION = settings.db_location

# Inizializzazione dei componenti
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
model = OllamaLLM(model=LLM_MODEL)

vectorstore = Chroma(
    collection_name="files",
    persist_directory=DB_LOCATION,
    embedding_function=embeddings
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

template = """
You are a helpful assistant. Answer the question based on the context provided.

Here is some relevant information: {context}

Here is the question: {question}
"""

def ask(question: str) -> Optional[str]:
    """
    Processes a question and returns an AI-generated answer based on the context.

    Args:
        question (str): The question to be answered.

    Returns:
        Optional[str]: The generated answer, or None if an error occurs.
    """
    try:
        logger.info(f"Received question: {question}")
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | model

        # Retrieve context from the vector store
        context = retriever.invoke(question)
        if not context:
            logger.warning("No relevant context found for the question.")
            return "I'm sorry, I couldn't find any relevant information to answer your question."

        # Generate the answer
        result = chain.invoke({"context": context, "question": question})
        logger.info("Answer generated successfully.")
        return result
    except Exception as e:
        logger.error(f"Error while processing the question: {e}")
        return None
