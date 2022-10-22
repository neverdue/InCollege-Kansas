import json
from webbrowser import get
from Code.Source.globalVariables import addPage, getFirst, getFriendsList, getIncomingRequests, getDataFile, getJobFile, getLast, getOutgoingRequests, getUser, getUserProfile, setProfileInfo, setExperienceInfo, getExperienceCount, setEducationInfo, getEducationCount
from Code.Source.globalVariables import PROFILE_KEYS, EXPERIENCE_KEYS, EDUCATION_KEYS
from Code.Source.menuOptions import back, goBackOption
from Code.Source.utility import addToFriendsList, createRequest, endProgram, inputValidation, checkLength, retrieveUser, printDivider, removeFromFriendsList, removeRequest, searchFilter, viewUser, writeJson, wJson, isDate, isDigit, continueInput

MAX_EXPERIENCE = 3 

def showHomePageGreeting():
    printDivider()
    print("Welcome to InCollege!")
    print("""Please choose from one of the options below:\n1. Search for a job\n2. Find someone you know\n3. Learn a new skill\n4. Useful Links\n5. InCollege Important Links\n6. Search Users
7. See incoming friend requests\n8. See outgoing friend requests\n9. Show my network\n{}\n11. Go to previously visited page\n""".format("10. Show your profile" if hasProfile(getUser()) else "10. Create your profile"))

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

def findSomeonePage():
    addPage(findSomeonePage)
    showConstructionMessage("Find someone you know")

def skillPage(skill):
    addPage(skillPage)
    showConstructionMessage("Learn a new skill")

def searchUsers():
    addPage(searchUsers)
    message = "\n1. Search by last name\n2. Search by major\n3. Search by university\n4. Previous Page\n"
    print(message)
    user_choice = inputValidation(1, 5)
    foundUsers = {}
    if user_choice == 1:
        foundUsers = searchFilter("lastName")
    elif user_choice == 2:
        foundUsers = searchFilter("major")
    elif user_choice == 3:
        foundUsers = searchFilter("university")
    elif user_choice == 4:
        back()

    if foundUsers != -1:
        print("Enter the username of the user you want to send a friend request.")
        user_choice = input("Enter your option: ")
        if user_choice in foundUsers:
            createRequest(getUser(), user_choice)
        else:
            print("Invalid input.")

def viewIncomingRequests():
    addPage(viewIncomingRequests)
    IncomingRequests = getIncomingRequests()
    length = len(IncomingRequests)
    while length > 0:
        if length == 1:
            print("\n\nYou have " + str(length) + " incoming request!\n")
        else:
            print("\n\nYou have " + str(length) + " incoming requests!\n")
        print("Incoming friend requests:")
        printDivider()
        for request in IncomingRequests:
            printDivider()
            viewUser(retrieveUser(request))
            printDivider()
        print("Enter the username of the user you want to select or enter 0 to go to homepage or -1 to exit.")
        user_choice = input("Enter your option: ")
        if user_choice == '0':
            back()
        elif user_choice == '-1':
            endProgram()
        if user_choice in IncomingRequests:
            print("1. Accept\n2. Decline")
            option = input("Enter your option: ")
            if option == '1':
                addToFriendsList(user_choice, getUser())
                print("Accepting request from {}...".format(user_choice))
                print("Request accepted!")
            elif option == '2':
                removeRequest(user_choice, getUser())
                print("Rejecting request from {}...".format(user_choice))
                print("Request rejected!")
            else:
                print("Invalid input.")
        else:
            print("Invalid input.")
        IncomingRequests = getIncomingRequests()
    printDivider()
    print("You have no incoming friend requests.")
    goBackOption()

def viewOutgoingRequests():
    addPage(viewOutgoingRequests)
    print("Outgoing friend requests:")
    printDivider()
    outgoingRequests = getOutgoingRequests()

    if len(outgoingRequests) == 0:
        print("You have no outgoing friend requests.")
        return
    
    printDivider()
    print("You have " + str(len(outgoingRequests)) + " outgoing requests!\n")
    printDivider()
    for request in outgoingRequests:
        printDivider()
        viewUser(retrieveUser(request))
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
    myNetwork = getFriendsList()

    if len(myNetwork) == 0:
        print("You have no friends.")
        return
        
    printDivider()
    print("You have " + str(len(myNetwork)) + " friends!\n")
    printDivider()
    for user in myNetwork:
        printDivider()
        viewUser(retrieveUser(user))
        printDivider()
    print("Enter the username of the user you want to unfriend or enter 0 to go back or -1 to exit.")
    user_choice = input("Enter your option: ")
    if user_choice == '0':
        back()
    elif user_choice == '-1':
        endProgram()
    if user_choice in myNetwork:
        removeFromFriendsList(getUser(), user_choice)

# PROFILE FUNCTIONS
def createProfile():
    addPage(createProfile)

    profile = getUserProfile()
    profileKeys = profile.keys()

    printDivider()
    print("Please enter the following information for your profile when prompted.")
    for key in PROFILE_KEYS:
        if key == "experience" and getExperienceCount() < MAX_EXPERIENCE: 
            addExperience()
            if not continueInput("continue filling out your profile"): break
        elif key == "education":
            addEducation()
            break
        elif key not in profileKeys:
            updateProfile(key)
            if not continueInput("continue filling out your profile"): break
    back()

def showProfile(): 
    addPage(showProfile)

    while True:
        printDivider()
        print("Your profile:")
        displayProfile(getUserProfile(), getFirst() + " " + getLast())

        print("\nEnter an option from 2-7 to replace your profile information.\nEnter 8 to go to previously visited page.")
        userInput = int(inputValidation(2, 9))
        if userInput == 8: break
        elif userInput in range(2, 6): 
            updateProfile(PROFILE_KEYS[userInput - 2])
        elif userInput == 6: 
            editProfile(PROFILE_KEYS[userInput - 2], EXPERIENCE_KEYS, getExperienceCount())
        else: 
            editProfile(PROFILE_KEYS[userInput - 2], EDUCATION_KEYS, getEducationCount())
    back()
    
# NOTE: Change how experience and education is displayed. Thank you!
def displayProfile(profile, name):
    print(f"1. Name: {name}")
    for count, key in enumerate(PROFILE_KEYS, start=2):
        print(f"{count}. {key.title()}: {profile[key]}")

# Use for profile's title, major, university, and about sections
def updateProfile(key):
    while True: 
        if key == "about":
            newInfo = input("\nEnter a paragraph about yourself: ")
        else: 
            newInfo = input(f"\nEnter your {key}: ")
        if checkLength(newInfo, 200, True): break
    if key == "major" or key == "university":
        newInfo = newInfo.title()

    setProfileInfo(key, newInfo)   # Update global variable
    updateProfileJson()            # Update json file

# Use for profile's experience and education section
def updateInfo(key, dict, keyword, helper): 
    print(f"\nEnter the following information about your past {key}:")
    newInfo = {}
    for keyName in dict:
        while True:
            userInput = input(f"Enter {keyName}: ")
            if checkLength(userInput, 200, True):
                # e.g. if asking for date, but user input is not in the date format "MM/DD/YYYY" keep asking again
                if keyword in keyName and not helper(userInput): continue
                newInfo[keyName] = userInput
                break
    return newInfo

def addExperience():
    while getExperienceCount() < MAX_EXPERIENCE: 
        if not continueInput("add a past job"): break
        newInfo = updateInfo("experience", EXPERIENCE_KEYS, "date", isDate)
        setExperienceInfo(newInfo)
        updateProfileJson()
    if getExperienceCount() == MAX_EXPERIENCE: 
        print("\nThe limit for past job experiences have been reached.")
            
def addEducation():
    while True: 
        newInfo = updateInfo("education", EDUCATION_KEYS, "years", isDigit)
        setEducationInfo(newInfo)
        updateProfileJson()
        if not continueInput("add another school"): break

# Use when replacing information from experience and education sections
def editProfile(key, dict, count): 
    print("\nEnter the number you want to replace. ")
    index = int(inputValidation(1, count+1))
    profile = getUserProfile()
    if key == "experience":
        profile[key][index-1] = updateInfo(key, dict, "date", isDate)
    else:
        profile[key][index-1] = updateInfo(key, dict, "years", isDigit)
    updateProfileJson()

def updateProfileJson():
    dataFile = getDataFile()
    with open(dataFile) as jsonFile:
        data = json.load(jsonFile)
        for account in data["accounts"]:
            if account["username"] == getUser():
                account["profile"] = getUserProfile() 
    wJson(data, dataFile)

# Get profile from username 
def getProfile(username): 
    dataFile = getDataFile()
    with open(dataFile) as jsonFile:
        data = json.load(jsonFile)
        for account in data["accounts"]:
            if account["username"] == username:
                return account["profile"]

# Check is user has profile
def hasProfile(username): 
    dataFile = getDataFile()
    with open(dataFile) as jsonFile:
        data = json.load(jsonFile)
        for account in data["accounts"]:
            if account["username"] == username and account["profile"]["education"]:
                return True 
    return False