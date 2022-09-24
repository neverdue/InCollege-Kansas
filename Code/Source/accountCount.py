#Checks if there are more than 5 or more accounts in the txt file
import json
def accountLimit(TESTMODE = False):
    userCount = 0
    if TESTMODE == False:
        dataFile = "accounts.json"
    else:
        dataFile = "accounts-test.json"
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            userCount+=1
    return userCount