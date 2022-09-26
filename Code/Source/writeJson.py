import json

def wJson(data, dataFile):
    with open(dataFile, "w") as json_file:
        json.dump(data, json_file, indent = 2)