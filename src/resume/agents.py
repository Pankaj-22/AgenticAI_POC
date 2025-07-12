from crewai_tools import FileReadTool , FileWriterTool
from crewai import Agent
# from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.0-flash-lite",
    temperature=0.7,
)

load_dotenv()

print("Using model:", os.getenv("GEMINI_MODEL_NAME"))
print("Using API key:", os.getenv("GEMINI_API_KEY"))

# Creating a resume summarizer agent with memory and verbose mode
Resume_Summarizer=Agent(
    role="Resume Summarizer",
    goal="Summarize the resume from given file into a concise and clear summary focusing on the key skills, experiences, and qualifications of the candidate",
    backstory="Expert analyst with a keen eye for detail",
    # memory=True,
    verbose=True,
    llm=llm,
    tools=[
        FileReadTool(file_path='user_resume.txt'),
        FileWriterTool(file_path='Resume_Summary.txt')
    ],
    thinking_steps=False,
    )