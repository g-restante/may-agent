from fastapi import APIRouter, UploadFile, HTTPException
from pydantic import BaseModel
from embedding import service
import logging

# Configurazione del logger
logger = logging.getLogger(__name__)

router = APIRouter()

class UploadStatus(BaseModel):
    """
    Response model for the upload endpoint.
    """
    id: str
    status: str

@router.post("/upload", response_model=UploadStatus, status_code=202)
async def upload(file: UploadFile) -> UploadStatus:
    """
    Uploads a file and processes it for embedding.

    Args:
        file (UploadFile): The file to be uploaded and processed.

    Returns:
        UploadStatus: The status of the upload and the file ID.

    Raises:
        HTTPException: If the file processing fails.
    """
    logger.info(f"Received file upload request: {file.filename}")
    try:
        outcome = await service.embedd_file(file)
        if not outcome:
            logger.warning(f"File processing failed: {file.filename}")
            raise HTTPException(
                status_code=400,
                detail="File upload failed. Please check the file format and try again."
            )
        logger.info(f"File successfully processed: {file.filename}")
        return UploadStatus(id=file.filename, status="success")
    except Exception as e:
        logger.error(f"Unexpected error while processing file {file.filename}: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred. Please try again later."
        )