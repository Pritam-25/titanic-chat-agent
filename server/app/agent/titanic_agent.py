import uuid
import base64
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
import seaborn as sns
from app.services.data_loader import load_titanic_data
from app.schemas.chat import ChatResponse
from langchain.agents.structured_output import ToolStrategy
from langchain_core.messages import ToolMessage

matplotlib.use("Agg")  # Use non-GUI backend for server environments

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable not set")

# Load dataset
df = load_titanic_data()

# --------------------------------------
# TOOL 1: Data Analysis 
# --------------------------------------
@tool
def analyze_data(query: str) -> str:
    """
    Use this tool to answer statistical or analytical questions
    about the Titanic dataset using pandas.
    """
    try:
        SAFE_GLOBALS = {"df": df, "pd": pd}
        SAFE_LOCALS = {}
        result = eval(query, SAFE_GLOBALS, SAFE_LOCALS)
        return str(result)
    except Exception as e:
        return f"Error analyzing data: {str(e)}"

# --------------------------------------
# TOOL 2: Plot Generator 
# --------------------------------------
@tool
def plot_data(code: str) -> str:
    """
    Use Seaborn for nicer visualizations.
    Provide code using dataframe 'df' and seaborn 'sns'.
    The plot will be saved automatically and returned as base64.
    """
    try:
        SAFE_GLOBALS = {"df": df, "plt": plt, "pd": pd, "sns": sns}
        plt.figure()
        exec(code, SAFE_GLOBALS)
        os.makedirs("app/static", exist_ok=True)
        filename = f"app/static/{uuid.uuid4()}.png"
        plt.tight_layout()  # improve spacing
        plt.savefig(filename, dpi=150)
        plt.close()

        # return filename only (keep binary data out of LLM/tool messages)
        return filename
    except Exception as e:
        return f"Plotting error: {str(e)}"


# -------------------------
# System prompt
# -------------------------
system_prompt = """
You are a professional data analyst on the Titanic dataset.
- For stats, use analyze_data
- For plots, use plot_data
Return user‑facing text for final answers only.
"""

# -------------------------
# LLM
# -------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,  # deterministic is better for tool calling
    api_key=api_key
)

# -------------------------
# Create Agent 
# -------------------------
agent = create_agent(
    llm,
    tools=[analyze_data, plot_data],
    system_prompt=system_prompt,
    response_format=ToolStrategy(ChatResponse)
)

# -------------------------
# Invoke Agent
# -------------------------
def run_agent(question: str) :
    response = agent.invoke({"messages": [{"role": "user", "content": question}]})
    result = response["structured_response"]
    # If the structured ChatResponse did not include an image, try to
    # recover any plot base64 returned by the `plot_data` tool in the
    # agent messages and attach it to the ChatResponse before returning.
    try:
        for msg in response["messages"]:
            if isinstance(msg, ToolMessage) and msg.name == "plot_data":
                tool_output = msg.content
                
                # New behavior: tool returns filename -> read file and convert to base64 here
                if tool_output.endswith(".png"):
                    try:
                        with open(tool_output, "rb") as fh:
                            b64 = base64.b64encode(fh.read()).decode("utf-8")
                        result.image_base64 = f"data:image/png;base64,{b64}"

                        # Delete file after successful encoding
                        os.remove(tool_output)

                        break
                    except Exception:
                        # If reading fails, continue searching other messages
                        continue
    except Exception:
        # Don't fail the whole call if recovery logic has an issue.
        pass

    return result