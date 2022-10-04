#Checks if the username is already taken
import json
from Code.Source.globalVariables import getDataFile

def accountExist(username):
    dataFile = getDataFile()
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            if(username == user): return 1
    return 0