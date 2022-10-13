import json
from Code.Source.globalVariables import addPage, getDataFile, getFirst, getFriends, getIncomingRequests, getJobFile, getLast, getLoggedUser, getOutgoingRequests, getUser, setFriends, setIncomingRequests, setOutgoingRequests
from Code.Source.menuOptions import back, goBackOption
from Code.Source.utility import acceptRequest, endProgram, getUserData, printDivider, rejectRequest, sendRequest, unFriend, updateUserAttribute, viewUser, writeJson


def showHomePageGreeting():
    printDivider()
    print("Welcome to InCollege!")
    print("""Please choose from one of the options below:\n1. Search for a job
2. Find someone you know\n3. Learn a new skill\n4. Useful Links\n5. InCollege Important Links\n6. Search Users\n7. See incoming friend requests\n8. See outgoing friend requests\n9. Show my network\n10. Go to previously visited page\n""")

def showSkillPageGreeting():
    printDivider()
    print("""Learn and explore the skill options below!\n1. Communication\n2. Leadership\n3. Collaboration\n4. Responsibility\n5. Time Management\n
Please enter a number from 1-5.\nEnter x to return to the home page.\nEnter y to go to previously visited page.\n""")

def showConstructionMessage(message):
    printDivider()
    print("We're sorry!\n'{}' feature is still under construction.\n".format(message))

def returnToHomePage():
    try:
        username = getUser()
    except:
        raise Exception("You are not logged in!")
    user_choice = input('Go back to homepage? (y/n): ')

    if user_choice == '-1' or user_choice == 'n':
        endProgram()

    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Please enter y for yes, n for no: ')
    if user_choice == 'y':
        return "homePage"
    else: 
        printDivider()
        exit

def jobPage():
    addPage(jobPage)

    message = "\n1. Post a job\n2. Home page\n3. Previous Page\n"
    print(message)
    user_choice = input("Enter your option: ")

    if user_choice == '-1':
        endProgram()

    while user_choice != '1' and user_choice != '2' and user_choice != '3':
        print("\nInvalid input.\n" + message)
        user_choice = input("Enter your option: ")
        if user_choice == '-1':
            endProgram()

    if user_choice == '1':
        addJobPost()
    elif user_choice == '2':
        return "homePage"
    elif user_choice == '3':
        back()

def addJobPost():
    fileName = getJobFile()

    #Checks if already 5 job posts
    with open (fileName) as jsonFile:
        data = json.load(jsonFile)
        temp1 = data["numPosts"]
        if temp1 >= 5:
            print("There are already five job posts. Try again later.")
            return

    print("Please input the following information about the job when prompted.\n")
    while True:
        jobTitle = input("Job Title: ")
        length = checkLength(jobTitle, 50)
        if length == True:
            break
    while True:
        jobDescription = input("Job Description: ")
        length = checkLength(jobDescription, 250)
        if length == True:
            break
    while True:
        jobEmployer = input("Employer: ")
        length = checkLength(jobEmployer, 50)
        if length == True:
            break
    while True:
        jobLocation = input("Job Location: ")
        length = checkLength(jobLocation, 50)
        if length == True:
            break
    while True:
        jobSalary = input("Job Salary: ")
        length = checkLength(jobSalary, 50)
        if length == True:
            break
    print("\n")

    jobDictionary = {
        "Title" : jobTitle,
        "Description" : jobDescription,
        "Employer" : jobEmployer,
        "Location" : jobLocation,
        "Salary" : jobSalary,
        "Name" : getFirst() + ' ' + getLast()
    }

    #Appends new post to json file, Increase post count if < 5
    with open (fileName) as jsonFile:
        data = json.load(jsonFile)
        temp = data["jobPosts"]
        y = jobDictionary
        temp.append(y)

        #increment number of job posts
        temp1 = data["numPosts"]
        data["numPosts"] = temp1 + 1
    
    writeJson(data, fileName)

#Read in job posts at application start upclear
def readJobPosts():
    fileName = getJobFile()
    with open(fileName) as json_file:
        data = json.load(json_file)
        jobPosts = data["jobPosts"]
    return jobPosts

#Character Limiter Function (Security Measure)
def checkLength(input, limit):
    if len(input) > limit:
        print("\nERROR: Maximum characters of " + str(limit) + " reached.\n")
        return False
    return True

def findSomeonePage():
    addPage(findSomeonePage)
    showConstructionMessage("Find someone you know")

def skillPage(skill):
    showConstructionMessage("Learn a new skill")

def searchByLastName():
    addPage(searchByLastName)
    print("Enter the last name of the user you are looking for.")
    lastName = input("Last Name: ")
    printDivider()
    print("Searching for {}...".format(lastName))
    printDivider()
    dataFile = getDataFile()
    foundUsers = {}
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            if user["lastName"] == lastName and user["username"] != getLoggedUser()["username"]:
                foundUsers[user["username"]] = user
                printDivider()
                viewUser(user)
                printDivider()
    if len(foundUsers) == 0:
        print("User not found.")
        return -1
    else:
        return foundUsers


def searchByMajor():
    addPage(searchByMajor)
    print("Enter the major of the user you are looking for.")
    major = input("Major: ")
    printDivider()
    print("Searching for {}...".format(major))
    printDivider()
    dataFile = getDataFile()
    foundUsers = {}
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            if user["major"] == major and user["username"] != getLoggedUser()["username"]:
                foundUsers[user["username"]] = user
                printDivider()
                viewUser(user)
                printDivider()
    if len(foundUsers) == 0:
        print("User not found.")
        return -1
    else:
        return foundUsers

            
def searchByUniversity():
    addPage(searchByUniversity)
    print("Enter the university of the user you are looking for.")
    university = input("University: ")
    printDivider()
    print("Searching for {}...".format(university))
    printDivider()
    dataFile = getDataFile()
    foundUsers = {}
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            if user["university"] == university and user["username"] != getLoggedUser()["username"]:
                foundUsers[user["username"]] = user
                printDivider()
                viewUser(user)
                printDivider()
    if len(foundUsers) == 0:
        print("User not found.")
        return -1
    else:
        return foundUsers  

def searchFilter(filterAttribute):
    print("Enter the {} of the user you are looking for.".format(filterAttribute))
    filterValue = input("{}: ".format(filterAttribute))
    printDivider()
    print("Searching for {}...".format(filterValue))
    printDivider()
    dataFile = getDataFile()
    foundUsers = {}
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            if user[filterAttribute] == filterValue and user["username"] != getLoggedUser()["username"] and user["username"] not in getOutgoingRequests():
                foundUsers[user["username"]] = user
                printDivider()
                viewUser(user)
                printDivider()
    if len(foundUsers) == 0:
        print("User not found.")
        return -1
    else:
        return foundUsers  


def searchUsers():
    addPage(searchUsers)
    message = "\n1. Search by last name\n2. Search by major\n3. Search by university\n4. Previous Page\n"
    print(message)
    user_choice = input("Enter your option: ")
    foundUsers = {}
    if user_choice == '1':
        foundUsers = searchFilter("lastName")
    elif user_choice == '2':
        foundUsers = searchFilter("major")
    elif user_choice == '3':
        foundUsers = searchFilter("university")
    elif user_choice == '4':
        back()

    if foundUsers != -1:
        print("Enter the username of the user you want to send a friend request.")
        user_choice = input("Enter your option: ")
        if user_choice in foundUsers:
            sendRequest(getLoggedUser(), foundUsers[user_choice])
            updatedOutgoingRequests = getOutgoingRequests()
            updatedOutgoingRequests.append(user_choice)
            setOutgoingRequests(updatedOutgoingRequests)

            updateUserAttribute(getLoggedUser(), "outgoingRequests", updatedOutgoingRequests)
        else:
            print("Invalid input.")

def viewIncomingRequests():
    addPage(viewIncomingRequests)
    IncomingRequests = getIncomingRequests()
    while len(IncomingRequests) > 0:
        print("\n\nYou have " + str(len(getIncomingRequests())) + " incoming requests!\n")
        print("Incoming friend requests:")
        printDivider()
        for request in IncomingRequests:
            printDivider()
            viewUser(getUserData(request))
            printDivider()
        print("Enter the username of the user you want to select or enter 0 to go to homepage or -1 to exit.")
        user_choice = input("Enter your option: ")
        if user_choice == '0':
            return "back"
        elif user_choice == '-1':
            endProgram()
        if user_choice in IncomingRequests:
            user1 = getLoggedUser()
            user2 = getUserData(user_choice)
            print("1. Accept\n2. Decline")
            option = input("Enter your option: ")
            if option == '1':
                acceptRequest(user1, user2)
            elif option == '2':
                rejectRequest(user1, user2)
            else:
                print("Invalid input.")
            updatedIncomingRequests = getIncomingRequests()
            updatedIncomingRequests.remove(user_choice)
            setIncomingRequests(updatedIncomingRequests)

            #Update User Settings
            updateUserAttribute(user1, "incomingRequests", updatedIncomingRequests)
        else:
            print("Invalid input.")
    print("You have no incoming friend requests.")
    goBackOption()

def viewOutgoingRequests():
    addPage(viewOutgoingRequests)
    print("Outgoing friend requests:")
    printDivider()
    outgoingRequests = getOutgoingRequests()
    for request in outgoingRequests:
        printDivider()
        viewUser(getUserData(request))
        printDivider()
    print("Enter 0 to go back or -1 to exit.")
    user_choice = input("Enter your option: ")
    if user_choice == '0':
        back()
    elif user_choice == '-1':
        endProgram()

def showMyNetwork():
    addPage(showMyNetwork)
    print("My Network:")
    printDivider()
    myNetwork = getFriends()
    if len(myNetwork) == 0:
        print("You have no friends.")
        return
    for user in myNetwork:
        printDivider()
        viewUser(getUserData(user))
        printDivider()
    print("Enter the username of the user you want to unfriend or enter 0 to go back or -1 to exit.")
    user_choice = input("Enter your option: ")
    if user_choice == '0':
        back()
    elif user_choice == '-1':
        endProgram()
    if user_choice in myNetwork:
        user1 = getLoggedUser()
        user2 = getUserData(user_choice)
        unFriend(user1, user2)
        updatedMyNetwork = getFriends()
        updatedMyNetwork.remove(user_choice)
        setFriends(updatedMyNetwork)

        #Update User Settings
        updateUserAttribute(user1, "friends", updatedMyNetwork)

        user2Network = user2["friends"]
        user2Network.remove(user1["username"])
        updateUserAttribute(user2, "friends", user2Network)