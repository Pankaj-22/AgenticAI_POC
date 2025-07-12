#AGENTIC AI POC Project : Project:Resume ATS Score Checker using CreAI framework

[Project:Resume ATS Score Checker](https://krishnaikacademy.notion.site/)

[gemini-api/docs/quickstart](https://ai.google.dev/gemini-api/docs/quickstart)

[gemini-api/docs/openai](https://ai.google.dev/gemini-api/docs/openai)



#Customize Your Project
```
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
```



##Your project will contain these essential files:

##File	Purpose <br>

agents.yaml	 --> Define your AI agents and their roles <br>
tasks.yaml	 --> Set up agent tasks and workflows <br>
.env	     --> Store API keys and environment variables <br>
main.py	     --> Project entry point and execution flow <br>
crew.py	     --> Crew orchestration and coordination <br>
tools/	     --> Directory for custom agent tools <br>
knowledge/	 --> Directory for knowledge base <br>

Start by editing agents.yaml and tasks.yaml to define your crew’s behavior. <br>

***Keep sensitive information like API keys in .env.

