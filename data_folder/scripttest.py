from langchain_google_genai import ChatGoogleGenerativeAI
import os

api_key = "YOUR_API_KEY"  # Replace with your actual API key
chat = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key="AIzaSyCiE6LLjrhG94AIhPAPV1CioP6xDA55o0M")

try:
    response = chat.invoke("Hello, how are you?")
    print(response)
except Exception as e:
    print(f"Error: {e}")