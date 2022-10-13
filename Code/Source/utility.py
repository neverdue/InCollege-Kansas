import json
from Code.Source.globalVariables import getDataFile

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
    try:
        inputSelection = int(input("Selection: "))
    except ValueError:
        raise Exception("Invalid input!")

    if inputSelection == -1:
        endProgram()

    while (inputSelection not in range(left, right)):
        print("Invalid selection, please try again.\n")
        try:
            inputSelection = int(input("Selection: "))
        except ValueError:
            raise Exception("Invalid input!")
    return inputSelection

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

def endProgram():
    print("Thank you for using InCollege!")
    exit()


#Utility function to get a user account object. Returned as a Dictionary.
def retrieveUser(username):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if username == search["username"].lower():
                #print(search)
                return search

#Gets users outgoingRequest list
def getUserOutgoingRequestList(username):
    #print(retrieveUser(username)["outgoingRequests"])
    return retrieveUser(username)["outgoingRequests"]


#Gets users incomingRequest list
def getUserIncomingRequestList(username):
    #print(retrieveUser(username)["incomingRequests"])
    return retrieveUser(username)["incomingRequests"]

#Returns users friendsList
def getUserFriendList(username):
    #print(retrieveUser(username)["friendsList"])
    return retrieveUser(username)["friendsList"]

#gets all users objects with a last name matching "lastName" parameter
def getUsersObjectsWithLastName(lastName):
    queryList = []
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if lastName.lower() == search["lastName"].lower():
                queryList.append(search)
    return queryList

#gets all usernames of users with last name matching "lastName" parameter
def getUsersByLastName(lastName):
    queryList = []
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if lastName.lower() == search["lastName"].lower():
                queryList.append(search["username"])


#gets all usernames of users with university matching "university" parameter
def getUsersByUniversity(university):
    queryList = []
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if university.lower() == search["university"].lower():
                #print(search["username"])
                queryList.append(search["username"])
    return queryList
    
#gets all usernames of users with major matching "major" parameter
def getUsersByMajor(major):
    queryList = []
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if major.lower() == search["major"].lower():
                queryList.append(search["username"])
    return queryList
       


#Functions of the form (loggedinuser,userbeinginteractedwith), no thought required 10/12/22
#These functions cover a lot of the same proccesses many times. I don't believe I can return a json object reference. will discuss in scrum - Rier 10/12/22
#Willing to discuss better ways to solve this if necessary, however going for the most intuitive approach first :)


#Updates request list of respective users
def createRequest(senderUsername, recipientUsername):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if senderUsername.lower() == search["username"].lower():
                print(recipientUsername, "was added to the outgoingRequests list for ", senderUsername)
                search["outgoingRequests"].append(recipientUsername)
                print(search["outgoingRequests"])
            elif recipientUsername == search["username"].lower():
                print(senderUsername, "was added to incomingRequests list for",recipientUsername)
                search["incomingRequests"].append(senderUsername)
                print(search["incomingRequests"])

    writeJson(data, dataFile)
    return


#Removes request list involving respective users
def removeRequest(incomingUsername, outgoingUsername):
    dataFile = getDataFile()
    with open(dataFile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            if incomingUsername.lower() == search["username"].lower():
                search["outgoingRequests"].remove(outgoingUsername)
            elif outgoingUsername.lower() == search["username"].lower():
                search["incomingRequests"].remove(incomingUsername)
    writeJson(data, dataFile)
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
    writeJson(data, dataFile)
    return





#TODO - Update existing users easier - did not find method that did so in brief look