from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import ask_agent

router = APIRouter()


@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
	try:
		response = ask_agent(request.question)
		return response
	except Exception as e:
		raise HTTPException(status_code=500, detail=str(e))
