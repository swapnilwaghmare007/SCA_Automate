import os
import subprocess

def check_and_run():
    if os.path.exists("workbook.xlsx"):
        print("Report found. Starting the SCA Assessment...")
        subprocess.run(["python3", "source/staging.py"])
    else:
        print("Report 'workbook.xlsx' not found.")
        print("Creating Report 'workbook.xlsx'...")
        subprocess.run(["python3", "xrayscan/reportcreate.py"])
        subprocess.run(["python3", "source/staging.py"])
       

if __name__ == "__main__":
    check_and_run()
