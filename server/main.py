import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.app:app",  # <folder>.<file>:<variable>
        host="0.0.0.0",
        port=8000,
        reload=True
    )