import requests
import json

# Define the base API URL
base_url = "https://security-cockpit.netcracker.com/api/v1"

# Read the JSON payload from a text file
with open("source/createwb/cockpitparams/payload.json", "r") as payload_file:
    payload = json.load(payload_file)

# Send the POST request to create a report
create_report_url = f"{base_url}/createreport"
response = requests.post(create_report_url, json=payload)

# Extract the buildid from the payload
buildid = payload.get("buildid")

# Write the extracted buildid to a file for future use
with open("source/createwb/cockpitparams/buildid.txt", "w") as buildid_file:
    buildid_file.write(buildid)

# Check if the report creation request was successful
if response.status_code == 200:
    try:
        response_json = response.json()
        print("POST request successful.")
        print("Response:", response_json)
    except requests.exceptions.JSONDecodeError:
        print("POST Response Successfull.")
        #print("Response Content:", response.text)
else:
    print("POST request failed. Status code:", response.status_code)
