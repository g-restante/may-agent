from fastapi import APIRouter
from pydantic import BaseModel
from ask import service

router = APIRouter()

class AnswerModel(BaseModel):
    code: str
    body: str

@router.get("", response_model=AnswerModel, status_code=200)
async def ask(question: str):
    answer = service.ask(question)
    return dict(
        code = "success",
        body = answer
    )