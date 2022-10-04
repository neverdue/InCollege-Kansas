import json
from Code.Source.globalVariables import getDataFile

def find(first, last):
    dataFile = getDataFile()
    
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for names in data["accounts"]:
            fName = names["firstName"]
            lName = names["lastName"]

            fName = fName.lower()
            lName = lName.lower()
            if first == fName and last == lName:
                return 1
        return 0