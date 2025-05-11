from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os

# TODO modify this to use parametrized settings
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "../chroma_langchain_db"
vectorstore = Chroma(
    collection_name="files",
    persist_directory=db_location,
    embedding_function=embeddings
    )

def embedd_file(file):
    outcome = False
    file_content = file.file.read()
    document = Document(
        page_content=file_content.decode("utf-8"),
        metadata={"filename": file.filename, 
                    "size": len(file_content),
                    "extension": file.filename.split(".")[-1]
                    },
        id = file.filename)
    vectorstore.add_documents(documents=[document], ids=[file.filename])
    outcome = True
    return outcome
