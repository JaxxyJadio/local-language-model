from fastapi import APIRouter
from pydantic import BaseModel
from backend.models.local_llm import generate_completion

router = APIRouter()

class LLMRequest(BaseModel):
    prompt: str

@router.post("/completion")
async def completion(request: LLMRequest):
    result = generate_completion(request.prompt)
    return {"completion": result}
