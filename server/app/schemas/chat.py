from pydantic import BaseModel, Field
from typing import Optional

class ChatRequest(BaseModel):
    question: str = Field(..., example="What is the Titanic?", min_length=3, max_length=500)

class ChatResponse(BaseModel):
    answer: str = Field(..., example="The Titanic was a British passenger liner that sank in the North Atlantic Ocean in 1912 after hitting an iceberg.")
    image_base64: Optional[str] = Field(None, example="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...")