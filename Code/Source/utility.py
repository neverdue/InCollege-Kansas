import json
import datetime
from Code.Source.globalVariables import getDataFile, getFriendsList, getIncomingRequests, getLoggedUser, getOutgoingRequests, getUser, getUserProfile, setFriendsList, setIncomingRequests, setOutgoingRequests, PROFILE_KEYS

#Checks all possible pages to call back to last page visited
def checkPages(page, links):
    if page in links:
        links[page]()
    else:
        print("ERROR. Page not found")

def printDivider():
    print('\n' + '-'*60 + '\n')

#Write data to a json File
def writeJson(data, filename):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4) 

def wJson(data, dataFile):
    with open(dataFile, "w") as json_file:
        json.dump(data, json_file, indent = 2)

def inputValidation(left, right):
    while True: 
        inputSelection = input("Selection: ")
        if inputSelection.isdigit(): 
            if int(inputSelection) in range(left, right): break
            if int(inputSelection) == -1:
                endProgram()
        print(f"Invalid input! Please enter a number from {left} to {right - 1}.")
    return int(inputSelection)

#Character Limiter Function (Security Measure)
def checkLength(input, limit, required=False):
    if len(input) > limit:
        print("\nERROR: Maximum characters of " + str(limit) + " reached.\n")
        return False
    if required and len(input) == 0: 
        print("\nERROR: No input entered.\n")
        return False
    return True

def accountExist(username):
    dataFile = getDataFile()
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            if(username == user): return 1
    return 0

# Returns 1 if all names are unique
# returns 0 if not

def unique():
    dataFile = getDataFile()
    
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        j = 1
        for names in data["accounts"]:
            fname = names["firstName"]
            lname = names["lastName"]
            fname = fname.lower()
            lname = lname.lower()

            #Check each first and last name with the first and last name of the next account
            for i in range(j, len(data["accounts"])):
                
                nextFname = data["accounts"][i]["firstName"]
                nextLname = data["accounts"][i]["lastName"]
                nextFname = nextFname.lower()
                nextLname = nextLname.lower()

                if fname == nextFname and lname == nextLname:
                    print("First and last names must be unique")
                    return 0
                #Outer loop name checked all names from inner loop. Move on to the next name to check
                if i >= len(data["acctounts"])-1:
                    j+=1
                    break
        return 1

def storyDisplay():
    print("'Hello, my name is Jane Doe and let me tell you how InCollege has paved a way to success for me.")
    print("Not too long ago, I was freshly graduated student that was having a tough time finding jobs and a direction in life.")
    print("As a freshly graduated student, I didn't have many accomplishments or connections that would help me land job interview,")
    print("but with the tools and connections that InCollege offered, i'm now well off as an independent adult with a strong career path in software engineering.")
    print("Not only am I a software engineer, i'm also now an ex-Navy SEAL, an ex-astronaught, and a part time neurosurgeon!")
    print("All of my accomplishments was stemmed off of me using InCollege. If you too sign up for InCollege, you can also be successful like me!")
    print("Thanks InCollege!'\n")

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

#Checks for minimum8 characters, maximum of 12 characters, 
#at least one capital letter, one digit, and one special character
def securePassword(password):
    capitalLetter, specialCharCnt, digit = 0, 0, 0

    specialCharacters = ('!','@','#','$', '%','^','&','*','(', ')','-','=','~','[',']',
                        '{','}','|',';',':',"'",',','<','>',".",'?','/')

    #Checks for password length
    if len(password) <= 7:
        print("Password minimum length not met: The password needs to be greater than 7 characters.")
        return
    elif len(password) > 12:
        print("Password maximum length exceeded: The password must be less than 13 characters.")
        return

    #Evaluates characters in the password
    for characters in password:
        for items in specialCharacters:
            if items in characters:
                specialCharCnt+=1
        if characters.isdigit() == 1:
            digit+=1
        elif characters.isupper() == 1:
            capitalLetter+=1

    if capitalLetter <= 0:
        print("Password needs to contain at least 1 capital letter.")
        return
    elif specialCharCnt <= 0:
        print("Password needs to contain at least 1 special character.")
        return
    elif digit <= 0:
        print("Password needs to contain at least 1 digit.")
        return
    return 1

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

def accountLimit():
    userCount = 0
    dataFile = getDataFile()
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            userCount+=1
    return userCount

def viewUser(user):
    print("Name: {} {}".format(user["firstName"], user["lastName"]))
    print("Username: {}".format(user["username"]))

def endProgram():
    print("Thank you for using InCollege!")
    exit()

#Utility function to get a user account object. Returned as a Dictionary.
def retrieveUser(username):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if username.lower() == search["username"].lower():
                return search

#Gets users outgoingRequest list
def getUserOutgoingRequestList(username):
    return retrieveUser(username)["outgoingRequests"]

#Gets users incomingRequest list
def getUserIncomingRequestList(username):
    return retrieveUser(username)["incomingRequests"]

#Returns users friendsList
def getUserFriendList(username):
    return retrieveUser(username)["friendsList"]

def searchFilter(filterAttribute):
    print("Enter the {} of the user you are looking for.".format(filterAttribute))
    filterValue = input("{}: ".format(filterAttribute.title()))
    printDivider()
    print("Searching for {}...".format(filterValue))
    printDivider()
    dataFile = getDataFile()
    foundUsers = {}
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

        #for each user in our account
        #Checks if attribute is in a profile key, and if 
        for user in data["accounts"]:
            #prevent from showing oneself in search
            if(user["username"] == getUser()):
                continue
            #check if the filter attribute is in the object 
            if(filterAttribute in user["profile"].keys() or filterAttribute in user.keys()):
                if(filterValue.lower() == user["profile"][filterAttribute].lower() or filterValue.lower() == user[filterAttribute].lower()):
                    foundUsers[user["username"]] = user
            else:
                continue
                
        # for user in data["accounts"]:
        #     if (((filterAttribute in user["profile"].keys() and user["profile"][filterAttribute].lower() == filterValue.lower()) 
        #      or (filterAttribute not in PROFILE_KEYS and user[filterAttribute].lower() == filterValue.lower()))
        #      and user["username"] != getUser() and user["username"] not in getOutgoingRequests() and 
        #      user["username"] not in getIncomingRequests() and user["username"] not in getFriendsList()):
        #         foundUsers[user["username"]] = user
                printDivider()
                viewUser(user)
                printDivider()
    if len(foundUsers) == 0:
        print("User not found.")
        return -1
    else:
        return foundUsers  


#Updates request list of respective users
def createRequest(senderUsername, recipientUsername):
    if isInFriendslist(recipientUsername):
        print("in friendslist already")
        return
    else:
        dataFile = getDataFile()
        with open(dataFile) as json_file:
            data = json.load(json_file)
            for search in data["accounts"]:
                if senderUsername.lower() == search["username"].lower():
                    search["outgoingRequests"].append(recipientUsername)
                elif recipientUsername.lower() == search["username"].lower():
                    search["incomingRequests"].append(senderUsername)
        print("Sending request to {}...".format(recipientUsername))
        print("Request sent!")
        writeJson(data, dataFile)
        setOutgoingRequests(getUserOutgoingRequestList(getUser()))
    return

def isInFriendslist(user):
    if user in getUserFriendList():
        return False
    else:
        return True

#Removes request list involving respective users
def removeRequest(senderUsername, recipientUsername):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if senderUsername.lower() == search["username"].lower():
                search["outgoingRequests"].remove(recipientUsername)
            elif recipientUsername.lower() == search["username"].lower():
                search["incomingRequests"].remove(senderUsername)
    writeJson(data, dataFile)
    setIncomingRequests(getUserIncomingRequestList(getUser()))
    return

#Updates respective users outgoing and incoming lists, and adds them to each other's friendsList
def addToFriendsList(senderUsername, recipientUsername):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if recipientUsername.lower() == search["username"].lower():
                search["friendsList"].append(senderUsername)
            elif senderUsername.lower() == search["username"].lower():
                search["friendsList"].append(recipientUsername)
    writeJson(data, dataFile)
    removeRequest(senderUsername, recipientUsername)
    setFriendsList(getUserFriendList(getUser()))
    return

#Removes users from each other's list, doesnt really matter what is put in what parameter, but it could be helpful.
def removeFromFriendsList(currentUser, personToRemove):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if currentUser.lower() == search["username"].lower():
                search["friendsList"].remove(personToRemove)
            elif personToRemove.lower() == search["username"].lower():
                search["friendsList"].remove(currentUser)
    print("Unfriending {}...".format(personToRemove))
    print("Unfriended!")
    writeJson(data, dataFile)
    setFriendsList(getUserFriendList(getUser()))
    return

def isDate(userInput):
    try:
        flag = bool(datetime.datetime.strptime(userInput, "%m/%d/%Y"))
    except ValueError:
        flag = False
        print("Incorrect input format, should be MM/DD/YYYY")
    return flag 

def isDigit(userInput):
    if userInput.isdigit():
        return True
    print("Please enter a number")
    return False 

def continueInput(message):
    while True: 
        userInput = input(f"\nDo you want to {message} (y/n): ")
        if userInput == "y":
            return True
        elif userInput == "n":
            return False
            
