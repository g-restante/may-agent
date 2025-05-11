from fastapi import APIRouter, UploadFile, HTTPException
from pydantic import BaseModel
from embedding import service

router = APIRouter()

class UploadStatus(BaseModel):
    code: str
    id: str

@router.post("/upload", response_model=UploadStatus, status_code=202)
async def upload(file: UploadFile):
    outcome = service.embedd_file(file)
    if not outcome:
        raise HTTPException(
            status_code=400,
            detail="File upload failed. Please check the file format and try again."
        )
    return dict(
        code = "success" if outcome else "failed",
        id=file.filename
    )