import os

from dotenv import load_dotenv
load_dotenv(override=True)

print("api key:", os.getenv("GOOGLE_API_KEY"))

from app.services.agent_service import ask_agent

question = "show me a histogram of ages"
question2 = "Can you analyze the survival rate of passengers by class and gender, explain the trends in detail, and show a visualization of survival percentages across Pclass and Sex?"

response = ask_agent(question2)

if response.image_base64:
    print("Image generated! Base64 length:", len(response.image_base64))

print("ans:", response.answer)
print("image:", response.image_base64)
