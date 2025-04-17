
from google.cloud import vision
import io
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

# Load the .env file
load_dotenv()


# Get the Google API key from .env
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment!")

#LLM INITIALIZATION 
# Initialize the Google Gemini model using LangChain

# "gemini-1.5-flash" is a good
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=google_api_key,
   
)

# Function to analyze image using Google Vision API (Unchanged)
def analyze_image(image_path):
   
    try:
        client = vision.ImageAnnotatorClient()
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()
        image = vision.Image(content=content)
        response = client.label_detection(image=image)

        if response.error.message:
             raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))

        labels = response.label_annotations
        return ", ".join([label.description for label in labels])
    except Exception as e:
        print(f"Error analyzing image with Vision API: {e}")
        return "Error analyzing image"


# Agent function (Unchanged logic, but uses the Gemini LLM now)
def agent_1(image_path, context_text=""):
    image_labels = analyze_image(image_path)
    if "Error analyzing image" in image_labels:
         # Handle the error appropriately, maybe return an error message
         # For now, let's try to proceed without image context or return error
         return "Could not analyze the image. Please describe the issue or try uploading again."

    prompt = f"The image shows labels: {image_labels}. The user says: '{context_text}'. Based on the image labels and the user's text, what issue could this be, and what should they do?"
    # The .invoke() method works similarly for LangChain integrations
    response = llm.invoke(prompt)
    # The response object might be slightly different. Often you need .content
    return response.content # Adjust if needed based on the specific response structure