from app.services.agent_service import ask_agent

question = "show me a histogram of ages"

response = ask_agent(question)

if response.image_base64:
    print("Image generated! Base64 length:", len(response.image_base64))

print("ans:", response.answer)
print("image:", response.image_base64)
