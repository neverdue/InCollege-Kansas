#Checks if there are more than 5 or more accounts in the txt file
import json
def accountLimit():
    userCount = 0
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            userCount+=1
    return userCount