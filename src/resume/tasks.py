from crewai import Task
from agents import Resume_Summarizer



Resume_Summarizer_Task= Task(  
      description = ("Summarize the resume into a concise and clear summary focusing on the key skills, experiences, and qualifications of the candidate and mention person's name"),
      agent = Resume_Summarizer,
      markdown = True,
      expected_output = "A 5 bullet point summary of the resume.",
      async_execution = False,
      verbose = True
  )