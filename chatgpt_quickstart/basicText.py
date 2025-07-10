from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

client = OpenAI()

input_text = input("Write your question or prompt here.")

response = client.responses.create(
    model="gpt-4.1",
    input=input_text
)

print(response.output_text)