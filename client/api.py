import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
API_URL = f"{BACKEND_URL}/api/v1/chat/"

def ask_backend(question: str):
    try:
        response = requests.post(
            API_URL,
            json={"question": question},
            timeout=60
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error calling backend: {e}")
        return {
            "answer": "Something went wrong, please try again later.",
            "image_base64": None
        }