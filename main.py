import os
import subprocess

def check_and_run():
    if os.path.exists("workbook.xlsx"):
        print("Report found. Starting the SCA Assessment...")
        subprocess.run(["python", "source/staging.py"])
    else:
        print("Report 'workbook.xlsx' not found.")
        print("Creating Report 'workbook.xlsx'...")
        subprocess.run(["python", "xrayscan/reportcreate.py"])
        subprocess.run(["python", "source/staging.py"])
       

if __name__ == "__main__":
    check_and_run()
