from app.agent.titanic_agent import run_agent
from app.schemas.chat import ChatResponse


def ask_agent(question: str) -> ChatResponse:
	"""Call the titanic agent and return a validated ChatResponse.

	Ensures the agent is not executed on import and normalizes the
	return value into a `ChatResponse`.
	"""
	result = run_agent(question)
	return result	
	


