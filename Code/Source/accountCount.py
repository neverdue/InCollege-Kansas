#Checks if there are more than 5 or more accounts in the txt file
import json
from Code.Source.globalVariables import getDataFile

def accountLimit():
    userCount = 0
    dataFile = getDataFile()
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            userCount+=1
    return userCount