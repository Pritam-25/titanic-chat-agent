# FastAPI server for the Titanic Chat Agent

Requirements

- Python 3.10+ (or as configured in your environment)
- Install dependencies from `pyproject.toml`:

manually: 

```bash
 cd server
 uv run
 .\.venv\Scripts\activate
```

Run

```bash
uvicorn app.app:app --reload
```

**API & Endpoints**

- Chat endpoint: POST to `/api/v1/chat` (see [server/app/api/v1/endpoints/chat.py](server/app/api/v1/endpoints/chat.py)).
- Router setup: [server/app/api/v1/router.py](server/app/api/v1/router.py).

