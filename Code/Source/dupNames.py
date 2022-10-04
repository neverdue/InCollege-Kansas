import json
from Code.Source.globalVariables import getDataFile

#checks first and last names and prevents duplicate first-last name combinations
def uniqueNames(first, last):
    dataFile = getDataFile()

    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

        first = first.lower()
        last = last.lower()

        for names in data["accounts"]:
            fname = names["firstName"].lower()
            lname = names["lastName"].lower()

            if first == fname and last == lname:
                print("Error: first and last name must be different than existing user's")
                return 0
    return 1