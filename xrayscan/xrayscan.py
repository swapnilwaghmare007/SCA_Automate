import json
import os
import re
from pprint import pprint
from sys import argv
import requests
import utils

scanParams = {"buildid": "REPLACEME", "applications": []}

def processFile(filename):
    ddfile = open(filename)
    dd = json.load(ddfile)
    if "component" not in dd["metadata"]:
        print("No component metadata found in %s" % filename)
        return
        
    application = {"name": dd["metadata"]["component"]}
    components = []

    for service in dd['services']:
        component = {
            "name": service["service_name"],
            "storage_items": [utils.resolveImage(service["full_image_name"])]
        }
        if "version" in service:
            component["version"] = service["version"]
        elif "git_branch" in service:
            component["version"] = service["git_branch"].replace("/", "-")
        elif "docker_tag" in service:
            component["version"] = service["docker_tag"]
        else:
            component["version"] = "Unknown"
            pprint(service)
            
        components.append(component)

    application["components"] = components
    appverPattern = r".+?deployment-artifacts-(.+?)\.json$"
    version = re.search(appverPattern, filename)
    if version is None:
        version = "Unknown"
    else:
        version = version.group(1)
    application["version"] = version
    scanParams["applications"].append(application)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: " + argv[0] + " file|directory")
        quit()

    if not os.path.exists(argv[1]):
        print("Path doesn't exist")
        quit()

    if os.path.isdir(argv[1]):
        for filename in os.listdir(argv[1]):
            processFile(os.path.join(argv[1], filename))
    else:
        processFile(argv[1])
        scanParams["buildid"] = scanParams["applications"][0]["version"]

    with open("source/createwb/cockpitparams/payload.json", "w") as output_file:
        json.dump(scanParams, output_file, indent=4)
