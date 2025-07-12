# src/resume_summary_generator/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import PDFReaderTool
from typing import List


@CrewBase
class ResumeSummaryGenerator(Crew):
    """
    Crew for generating resume summaries.
    """
    # agents: List[BaseAgent]
    # tasks: List[Task]
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def analyst(self) -> Agent:
        return Agent(
        config=self.agents_config['resume_summarizer'],
        tools=[PDFReaderTool()],
        verbose=True
        )

    @task
    def summarizer_task(self) -> Task:
        return Task(
        config=self.tasks_config['resume_summarizer_task'],
        tools=[PDFReaderTool()],
        output_file='output/summary.md' # This is the file that will be contain the final report.
        )
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
