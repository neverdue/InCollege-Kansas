from Code.Source.accountCount import accountLimit
from Code.Source.accountCheck import accountExist
from Code.Source.passwordCheck import securePassword
import json
import writeJson

#Create a prompt that asks a user to input their username and password

#Takes user input for username and password
#Stores concatenated user and password separated by a space into a file

#Dependent on other functions each imported from their own file

#################################################################
# 9/22/22 altered functions to also take first+last name
# replaced account text file with json file

# QUESTION: When we create an account, the system needs to check if there are 5 or more accounts.
#           When it does check during account creation, it still requests first name and last name
#           The issue that occurs that its wasted time if there are 5 accounts but on the 6th, the system still asks for first + last name
#           The funtionality still works, but it doesn't make sense for it still to ask for first and last name during the 6th account checking
#           Now this may be fine since Epic2 doesn't specify if this is an issue or not

# QUESTION: Should we convert all user input to lower/upper case for ease of checking in other functions?
#################################################################


def register(username, password, first, last): 
    if accountExist(username) == 1:
        print("Username {} already exists, please try again.".format(username)) 
        return
    if accountLimit() >= 5:
        print("All permitted accounts have been created, please come back and try later.")
        return

    while securePassword(password) != 1:
        password = input("Enter password: ")
    
    print("You have successfully registered.")

    #Adding credentials + names to json
    with open("accounts.json") as json_file:
        data = json.load(json_file)
        temp = data["accounts"]
        newData = {"username": username, "password" : password, "firstName" : first, "lastName" : last}
        temp.append(newData)

    writeJson.wJson(data)
    return 1

def login(username, password):
    exitLoop = 0
    if accountExist(username) != 1: 
        print("User does not exist.")
        return

    while exitLoop != 1:
        #scanning file
        if verifyCredentials(username, password) != 1:
            print("Incorrect username / password, please try again.")
            username = input("Enter username: ")
            password = input("Enter password: ")
        else:
            print("You have successfully logged in.")
            exitLoop = 1
    return 1

def verifyCredentials(usernameInput, passwordInput):
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            password = items["password"]
            if usernameInput == user and passwordInput == password:
                return 1
    return 0

