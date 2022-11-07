import json
from Code.Source.utility import accountLimit, accountExist, securePassword, wJson, uniqueNames
from Code.Source.globalVariables import getDataFile, getLoggedUser, userInit, getTimer
import time

#Create a prompt that asks a user to input their username and password

def signUpPage():
    if getLoggedUser() != None:
        raise Exception("You are already logged in.")

    if accountLimit() >= 10:
        print("All permitted accounts have been created, please come back and try later.")
        return

    username = input("Enter username: ")
    password = input("Enter password: ")
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    subscription = input("Would you like to subscribe to become a plus member for $10 a month?\n\t*As a plus member you can send and receive messages from anyone in the InCollege system*\n\t\t\t*rather than only users you are friends with*\n(yes/no): ")
    
    while subscription != "yes" and subscription != "no":
        subscription = input("Invalid input. Please input 'yes' or 'no': ")
    while(uniqueNames(firstname, lastname) == 0):
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")

    if subscription == "yes":
        subscription = True
        print("We will start to bill you $10 monthly. Thank you for becoming a PLUS member!")
    else:
        subscription = False
    # successful registration returns 1
    registrationAttempt = register(username, password, firstname, lastname, subscription)

    return registrationAttempt

def register(username, password, first, last, subscription):
    dataFile = getDataFile()

    if accountExist(username) == 1:
        print("Username {} already exists, please try again.".format(username)) 
        return
    if accountLimit() >= 10:
        print("All permitted accounts have been created, please come back and try later.")
        return

    while securePassword(password) != 1:
        password = input("Enter password: ")
    
    #Adding credentials, names, and default settings to json
    with open(dataFile) as json_file:
        data = json.load(json_file)
        temp = data["accounts"]
        newData = {"username": username, "password" : password, "firstName" : first, "lastName" : last,
         "language": "English", "email": setting(True), "SMS": setting(True), "ads": setting(True), "subscription": setting(subscription),
         "incomingRequests": [], "outgoingRequests": [], "friendsList": [], "profile": {"experience": [], "education": []}}
        temp.append(newData)

    wJson(data, dataFile)

    print("You have successfully registered.")
    timer = getTimer()
    time.sleep(timer)

    userInit(username, first, last, "English", True, True, True, subscription, [], [], [], {"experience": [], "education": []})

    return 1

def login(username, password):
    exitLoop = 0

    dataFile = getDataFile()

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
            timer = getTimer()
            time.sleep(timer)
            exitLoop = 1
    
    #get logged in user's data and settings
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            tempUser = items["username"]
            if username == tempUser:
                firstname = items["firstName"]
                lastname = items["lastName"]
                incomingRequests = items["incomingRequests"]
                outgoingRequests = items["outgoingRequests"]
                friendsList = items["friendsList"]
                language = "English" if items["language"] == "English" else "Spanish"
                email = True if items["email"] == "True" else False
                SMS = True if items["SMS"] == "True" else False 
                ads = True if items["ads"] == "True" else False
                subscription = True if items["subscription"] == "True" else False
                profile = items["profile"]

    #set user variable
    userInit(username, firstname, lastname, language, email, SMS, ads, subscription, incomingRequests, outgoingRequests, friendsList, profile)

    return 1

def verifyCredentials(usernameInput, passwordInput):
    dataFile = getDataFile()

    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            password = items["password"]
            if usernameInput == user and passwordInput == password:
                return 1
    return 0

def setting(flag):
    return "True" if flag == True else "False"