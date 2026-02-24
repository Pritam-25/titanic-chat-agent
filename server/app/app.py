from dotenv import load_dotenv
load_dotenv(override=True)

from fastapi import FastAPI
from .api.v1.router import api_router


app = FastAPI(title="Titanic Chat Agent")

app.include_router(api_router, prefix="/api/v1")  # Include the API router with a prefix

@app.get("/")
async def root():
    return {"message": "Hello World"}