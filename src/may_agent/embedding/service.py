from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from files.audio import service as audio_service
from files.img import service as img_service
from utils import utils
from settings import settings
import filetype
import logging
from typing import Any

logger = logging.getLogger(__name__)

EMBEDDING_MODEL = settings.embedding_model
DB_LOCATION = settings.db_location

vectorstore = Chroma(
    collection_name="files",
    persist_directory=DB_LOCATION,
    embedding_function=EMBEDDING_MODEL
)

async def embedd_file(file: Any) -> bool:
    """
    Embeds a file into the vector store after processing its content.

    Args:
        file (Any): The file object to process.

    Returns:
        bool: True if the file was successfully embedded, False otherwise.
    """
    try:
        content = await file.read()
        file.file.seek(0)

        if filetype.is_audio(content):
            logger.info(f"Processing audio file: {file.filename}")
            text = audio_service.transcribe_audio(file.file)
        elif filetype.is_image(content):
            logger.info(f"Processing image file: {file.filename}")
            text = img_service.ocr_image(content)
        elif utils.is_text_file(content):
            logger.info(f"Processing text file: {file.filename}")
            file_content = file.file.read()
            text = file_content.decode("utf-8")
        else:
            logger.warning(f"Unsupported file type: {file.filename}")
            return False

        return create_document(file, text)
    except Exception as e:
        logger.error(f"Error processing file {file.filename}: {e}")
        return False

def create_document(file: Any, text: str) -> bool:
    """
    Creates a document and adds it to the vector store.

    Args:
        file (Any): The file object containing metadata.
        text (str): The processed text content of the file.

    Returns:
        bool: True if the document was successfully created and added.
    """
    try:
        document = Document(
            page_content=text,
            metadata={
                "filename": file.filename,
                "extension": file.filename.split(".")[-1]
            },
            id=file.filename
        )
        vectorstore.add_documents(documents=[document], ids=[file.filename])
        logger.info(f"Document added to vector store: {file.filename}")
        return True
    except Exception as e:
        logger.error(f"Error creating document for file {file.filename}: {e}")
        return False
