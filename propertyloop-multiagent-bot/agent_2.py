# agent2.py
from dotenv import load_dotenv
import os
# --- MODIFIED IMPORT ---
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# --- MODIFIED KEY LOADING ---
# Get the Google API key
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment!")

# --- MODIFIED LLM INITIALIZATION ---
# Initialize ChatGoogleGenerativeAI with explicit API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", # Or another suitable Gemini model
    google_api_key=google_api_key
    # Optional: Add safety settings here too if needed
)

# Agent function (Unchanged logic, but uses the Gemini LLM now)
def agent_2(user_query, location=None):
    prompt = f"The user asked: '{user_query}'. The user's location is: '{location or 'Unknown'}'. Give tenancy advice accordingly."
    # The .invoke() method works similarly
    response = llm.invoke(prompt)
    # Extract content from the response object
    return response.content # Adjust if needed