from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
import os

# TODO modify this to use parametrized settings
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
model = OllamaLLM(model="llama3.2")

db_location = "../chroma_langchain_db"
vectorstore = Chroma(
    collection_name="files",
    persist_directory=db_location,
    embedding_function=embeddings
    )
retriver = vectorstore.as_retriever(search_kwargs={"k": 5})

template = """
You are a helpful assistant. Answer the question based on the context provided.

Here some revelant information: {context}

Here is the question: {question}
"""

def ask(question):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    answer = retriver.invoke(question)
    result = chain.invoke({"context": answer, "question": question})
    return result
