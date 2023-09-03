import os
import time
import subprocess

# Dictionary containing script names and their corresponding messages
script_messages = {
    "source/Prog1.py": "\nStarting the Assessment.\nDeleting False Postives,  Low & Medium Severity and Fixed Version as Blank\n",
    "source/Prog2.py": "\nUpdating Vectors for Microservices from Dataset.\n",
    "source/Prog6.py": "\nUpdating NC Severity from modified NC Score.\n",
    "source/Prog7.py": "\nChecking for Vulnerabilities which need Vendor Fix\n",
    "source/Prog3.py": "\nUpdating Vectors for Packages from Dataset\n",
    "source/Prog5.py": "\nUpdating Score from First.org. This may take couple of minutes...\n",
    "source/Prog8.py": "\nSorting Report based on NC Severity\n",
    "source/Prog4.py": "\nChecking for Blank Records...\n"
}

def run_script(script_name, delay_seconds):
    message = script_messages.get(script_name, "Running Script")
    print(message)
    time.sleep(delay_seconds)
    subprocess.call(["python", script_name])

def main():
    scripts_to_run = ["source/Prog1.py", "source/Prog2.py" , "source/Prog3.py", "source/Prog4.py", "source/Prog5.py", "source/Prog6.py", "source/Prog7.py", "source/Prog8.py"]
    delay_seconds = 2

    for script in scripts_to_run:
        run_script(script, delay_seconds)
        #input(f"Press Enter to run the next program, or Ctrl+C to exit.")

if __name__ == "__main__":
    main()
