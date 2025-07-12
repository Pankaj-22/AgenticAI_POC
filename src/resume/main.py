#!/usr/bin/env python

from crew import crew


def run():
    """
    Run the crew.
    """    
    try:
        outputs = crew.kickoff()
        print("Crew outputs:", outputs)
    except Exception as e: 
        import traceback
        print("🔴 Exception occurred:")
        traceback.print_exc()

if __name__ == "__main__":
    run()


 # inputs = {"pdf_path": os.path.join("knowledge", "Latest_Resume.pdf")}