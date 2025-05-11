from fastapi import APIRouter
from pydantic import BaseModel
from ask import service

router = APIRouter()

class AnswerModel(BaseModel):
    status: str
    body: str

@router.get("/ask", response_model=AnswerModel, status_code=200)
async def ask(question: str):
    answer = service.ask(question)
    return dict(
        status = "success",
        body = answer
    )