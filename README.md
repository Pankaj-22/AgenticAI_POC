#AGENTIC AI POC Project : Project:Resume ATS Score Checker using CreAI framework

[Project:Resume ATS Score Checker](https://krishnaikacademy.notion.site/)

[gemini-api/docs/quickstart](https://ai.google.dev/gemini-api/docs/quickstart)

[gemini-api/docs/openai](https://ai.google.dev/gemini-api/docs/openai)



#Customize Your Project

my_project/
├── .gitignore
├── knowledge/
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml



##Your project will contain these essential files:

File	Purpose
agents.yaml	Define your AI agents and their roles
tasks.yaml	Set up agent tasks and workflows
.env	Store API keys and environment variables
main.py	Project entry point and execution flow
crew.py	Crew orchestration and coordination
tools/	Directory for custom agent tools
knowledge/	Directory for knowledge base
Start by editing agents.yaml and tasks.yaml to define your crew’s behavior.

Keep sensitive information like API keys in .env.

