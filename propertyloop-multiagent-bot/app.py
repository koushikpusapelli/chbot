import streamlit as st
from agent_1 import agent_1
from agent_2 import agent_2
from router import route_input
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

st.title("🏘️ PropertyLoop Multi-Agent Chatbot by Koushik")

user_input = st.text_input("Enter your query:")
image_file = st.file_uploader("Upload an image (optional)")
location = st.text_input("City or region (optional)")

if st.button("Submit"):
    if image_file:
        with open("uploaded.jpg", "wb") as f:
            f.write(image_file.read())
        response = agent_1("uploaded.jpg", user_input)
    else:
        route = route_input(user_input, has_image=False)
        if route == "agent_2":
            response = agent_2(user_input, location)
        else:
            response = "Please upload an image or ask a tenancy-related question."
    
    st.write("🤖", response)

