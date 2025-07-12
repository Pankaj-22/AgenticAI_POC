# src/resume_summary_generator/main.py

from crew import ResumeSummaryGenerator

def run():
    inputs = {"pdf_path": "knowledge\Latest_Resume.pdf"}
    ResumeSummaryGenerator().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()