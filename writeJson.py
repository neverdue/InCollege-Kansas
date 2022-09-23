import json

def wJson(data):
    with open("accounts.json", "w") as json_file:
        json.dump(data, json_file, indent = 2)