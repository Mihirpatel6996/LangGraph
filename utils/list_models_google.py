import os
from dotenv import load_dotenv
from google import genai

# Load the GEMINI_API_KEY from your .env file
load_dotenv()

# Initialize the Google GenAI client (automatically finds your key)
client = genai.Client()

# Fetch and print all available models
print("Available Gemini Models:")
for model in client.models.list():
    print(model.name)