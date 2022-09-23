#Checks if the username is already taken
import json
def accountExist(username):
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            if(username == user): return 1
    return 0