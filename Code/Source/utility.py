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



#TODO - Update existing users easier - did not find method that did so in brief look