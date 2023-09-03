import os
import subprocess

def main():
    json_path = input("Enter the JSON path: ")

    if not os.path.exists(json_path):
        print("JSON file does not exist.")
        return

    xrayscan_command = f'python xrayscan/xrayscan.py "{json_path}"'
    
    try:
        subprocess.run(xrayscan_command, shell=True, check=True)
        
        
        create_scripts = ['source/createwb/POSTCockpit.py', 'source/createwb/GETStatus1.py', 'source/createwb/GETReport.py']
        
        for script in create_scripts:
            subprocess.run(f'python {script}', shell=True, check=True)
            
    except subprocess.CalledProcessError as e:
        print("An error occurred while running the scripts.")
        print(e)

if __name__ == "__main__":
    main()
