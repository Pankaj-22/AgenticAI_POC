from crewai import Crew,Process
from tasks import Resume_Summarizer_Task
from agents import Resume_Summarizer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[Resume_Summarizer],
    tasks=[Resume_Summarizer_Task],
    process=Process.sequential,

)