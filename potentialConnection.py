import json

def find(first, last, TESTMODE = False):
    if TESTMODE == False:
        dataFile = "accounts.json"
    else:
        dataFile = "accounts-test.json"
    
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