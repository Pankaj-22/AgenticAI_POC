from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

user_input = input("Enter your query: ")

# model="gemini-2.0-flash-lite" # no thinking capabilities
response = client.models.generate_content(
    # model="gemini-2.5-flash",
    model="gemini-2.0-flash-lite",
    contents=user_input,
)
print(response.text)

# model="gemini-2.5-flash" # have thinking capabilities
# response = client.models.generate_content(
#     model="gemini-2.5-flash",
#     contents=user_input,
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
#     ),
# )
# print(response.text)