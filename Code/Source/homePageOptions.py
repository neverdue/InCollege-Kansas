from getpass import getuser
import json
import datetime
from socket import getnameinfo
from webbrowser import get
from Code.Source.globalVariables import addPage, getApplicationsFile, getFirst, getFriendsList, getIncomingRequests, getDataFile, getJobFile, getLast, getOutgoingRequests, getUser, getUserProfile, setProfileInfo, setExperienceInfo, getExperienceCount, setEducationInfo, getEducationCount, getLoggedUser
from Code.Source.globalVariables import PROFILE_KEYS, EXPERIENCE_KEYS, EDUCATION_KEYS
from Code.Source.menuOptions import back, goBackOption
from Code.Source.utility import addToFriendsList, createRequest, endProgram, inputValidation, checkLength, retrieveUser, printDivider, removeFromFriendsList, removeRequest, searchFilter, viewUser, writeJson, wJson, isDate, isDigit, continueInput

MAX_EXPERIENCE = 3 

def showHomePageGreeting():
    printDivider()
    print("Welcome to InCollege!")
    print("""Please choose from one of the options below:\n1. Search for a job\n2. Find someone you know\n3. Learn a new skill\n4. Useful Links\n5. InCollege Important Links\n6. Search Users
7. See incoming friend requests\n8. See outgoing friend requests\n9. Show my network\n10. Your profile\n11. Go to previously visited page\n""")

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

    message = "\n1. Post a job\n2. Home page\n3. See all job posts\n4. Previous Page\n"
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
        showAllJobs()
    elif user_choice == '4':
        back()

def addJobPost():
    fileName = getJobFile()

    #Checks if already 5 job posts
    with open (fileName) as jsonFile:
        data = json.load(jsonFile)
        temp1 = data["numPosts"]
        if temp1 >= 10:
            print("There are already ten job posts. Try again later.")
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

    tempID = data["currentIDs"]##
    jobDictionary = {
        "id" : str(tempID + 1), ##
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

        #increment job ID's to keep track of new jobs
        data["currentIDs"] = tempID + 1 ##
    
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
        length = len(IncomingRequests)
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

#"Show my Network - displays a friend network and interaction options with users in that network"
def showMyNetwork():
    addPage(showMyNetwork)
    print("My Network:")
    printDivider()
    myNetwork = getFriendsList()
        
    if len(myNetwork) == 0:
        print("You have no friends. :(")
        return
        
    printDivider()
    print("You have " + str(len(myNetwork)) + " friends!\n")
    printDivider()
    for user in myNetwork:
        printDivider()
        viewUser(retrieveUser(user))
        printDivider()
    
    #Prompts user to select a person to interact with, or exit the program.
    user_choice = input("You may select a user from the network to interact with, press 0 to go Home, or -1 to exit")
    selectedUser = None
    #while an option wasn't pressed that leads to another page function
    while user_choice != '-1' and user_choice != '0' and selectedUser == None:
        if user_choice in myNetwork:
            selectedUser = user_choice
            print(f"Selected User is: {selectedUser}")  
        else:
            print("Username you tried to select does not exist or was spelt incorrectly.")
            user_choice = input("You may select a user from the network to interact with, press 0 to go Home, or -1 to exit")
    else:
        #any backPage options, could have a list or something to make this easier
        if user_choice == '0':
            back()
        elif user_choice == '-1':
            endProgram()
        else:
            canRemoveSelectedUser = True
            #if hasprofile, we go through these menu options for them
            while user_choice != '-1' and user_choice != '0':
                print(f"Choose an interaction option for: {selectedUser}")
                #reset displayHolderString after each option is processsed
                displayHolderString = ""
                #if has profile append option to display
                if hasProfile(selectedUser):
                    displayHolderString += "Interaction options: 1. View Profile,"

                if canRemoveSelectedUser:
                    displayHolderString += "2. Remove friend from MyNetwork,"
                displayHolderString+= "0. go back home, -1 exit application"

                print(displayHolderString)   
                user_choice = input("Enter your option: ")
                #if select profile option
                if(user_choice == '1'):
                    if(hasProfile(selectedUser)):
                        print(f"Viewing {selectedUser}'s profile" )
                        selectedUserProfile = getProfile(selectedUser)
                        selectedUserAccount = retrieveUser(selectedUser)
                        displayProfile(selectedUserProfile, selectedUserAccount["firstName"] +" " + selectedUserAccount["lastName"] )
                elif(user_choice == '2'):
                    if(canRemoveSelectedUser == True):
                        removeFromFriendsList(getUser(), selectedUser)
                        canRemoveSelectedUser = False   
                    #make them exit, because they should not be able to see info if unfriended
                    user_choice = '0'
            else:
                if(user_choice == '0'):
                    back()
                elif(user_choice == '-1'):
                    endProgram()


# PROFILE FUNCTIONS
def createProfile():
    profile = getUserProfile()
    profileKeys = profile.keys()

    printDivider()
    print("Please enter the following information for your profile when prompted.")
    for key in PROFILE_KEYS:
        if key == "experience" and getExperienceCount() < MAX_EXPERIENCE: 
            addExperience()
            if not continueInput("continue filling out your profile"): back()
        elif key == "education":
            addEducation()
            back()
        elif key not in profileKeys:
            updateProfile(key)
            if not continueInput("continue filling out your profile"): back()

def showProfile():
    while True:
        printDivider()
        print("Your profile:")
        displayProfile(getUserProfile(), getFirst() + " " + getLast())

        print("Enter an option from 2-7 to replace your profile information.\nEnter 8 to go to previously visited page.")
        userInput = int(inputValidation(2, 9))
        if userInput == 8: back()
        elif userInput in range(2, 6): 
            updateProfile(PROFILE_KEYS[userInput - 2])
        elif userInput == 6: 
            editProfile(PROFILE_KEYS[userInput - 2], EXPERIENCE_KEYS, getExperienceCount())
        else: 
            editProfile(PROFILE_KEYS[userInput - 2], EDUCATION_KEYS, getEducationCount())
    
def displayProfile(profile, name):
    print(f"1. Name: {name}")
    for count, key in enumerate(PROFILE_KEYS, start=2):
        #For displaying elements of objects that the profile contains
        if(key == "experience" or key == "education"):
            print(f"{count}. {key.title()}:")
            for index, key2 in enumerate(profile[key], start=1):
                print(f"\t{key.title()} #{index}:")
                keyList = EXPERIENCE_KEYS if key == "experience" else EDUCATION_KEYS
                for expKey in keyList:
                    print(f"\t{expKey.title()}: {key2[expKey]}")
                print()
        else:
            print(f"{count}. {key.title()}: {profile[key]}")

# Use for profile's title, major, university, and about sections
def updateProfile(key):
    while True: 
        if key == "about":
            # newInfo = input("\nEnter a paragraph about yourself: ")
            print("\nEnter a paragraph about yourself: ", end='')
        else: 
            # newInfo = input(f"\nEnter your {key}: ")
            print(f"\nEnter your {key}: ", end='')
        newInfo = input()
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
            print(f"Enter {keyName}: ", end='')
            userInput = input()
            # userInput = input(f"Enter {keyName}: ")
            if checkLength(userInput, 200, True):
                # e.g. if asking for date, but user input is not in the date format "MM/DD/YYYY" keep asking again
                if keyword in keyName and not helper(userInput): continue
                newInfo[keyName] = userInput
                break
    return newInfo

def addExperience():
    while getExperienceCount() < MAX_EXPERIENCE: 
        if not continueInput("add a past job"): return
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
        if not continueInput("add another school"): return 

# Use when replacing information from experience and education sections
def editProfile(key, dict, count): 
    print(f"\nEnter the number of {key} you want to replace. ")
    index = int(inputValidation(1, count+1)) - 1
    profile = getUserProfile()
    if key == "experience":
        profile[key][index] = updateInfo(key, dict, "date", isDate)
    else:
        profile[key][index] = updateInfo(key, dict, "years", isDigit)
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
    return retrieveUser(username)["profile"]

# Check is user has profile
def hasProfile(username): 
    return True if getProfile(username)["education"] else False

# Menu for user interactions with profile
def profilePage():
    addPage(profilePage)
    printDivider()
    print("Press 1 to create profile, 2 to view it")
    user_choice = input("Selection: ")
    if(user_choice == '1'):
        showProfile() if hasProfile(getUser()) else createProfile()
    elif(user_choice == '2'):
        if hasProfile(getUser()):
            displayProfile(getProfile(getUser()) ,(getLoggedUser()["firstName"] + " " + getLoggedUser()["lastName"]))
        else:
            print("Profile not found")

#def showJobDetails(entry):

# Shows list of posted jobs from json jobs file
def showAllJobs():
    filename = getJobFile()
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        count = 0
        # Showing list of job titles
        ############################################
        for items in data["jobPosts"]:
            jobID = data["jobPosts"][1]["id"]
            with open(getApplicationsFile()) as json_file2:
                data2 = json.load(json_file2)
                temp = data2
                if jobID in temp[getUser()]:
                    count+=1
                    print(jobID in temp[getUser()])
                    print(str(count) + ". " + items["Title"] +  " (applied)")
                    continue
                elif jobID not in temp[getUser()]:
                    count+=1
                    print(jobID in temp[getUser()])
                    print(str(count) + ". " + items["Title"])
        ##############################################
        print("\nEnter a value from {} to {} to view job posting or -1 to quit: ".format("1", str(count)))
        userInput = str(inputValidation(1,11))

        # Showing details of the job selected
        for i in data["jobPosts"][int(userInput)-1]:
            # Don't show job ID
            if(i == "id"): continue
            print(i + " : " + data["jobPosts"][int(userInput)-1][i])
        
        print("\nWould you like to apply for this job? Enter 1 to apply or 2 to cancel.")
        applyJob = str(inputValidation(1,3))
        if applyJob == '1':
            # Checking if the applicant is also the poster
            fullName = getFirst() + " " + getLast()
            if fullName == data["jobPosts"][int(userInput)-1]["Name"]:
                print("You can't apply to a job you've posted")
            # Writing info about applicant to applications json
            else:
                jobID = data["jobPosts"][int(userInput)-1]["id"]
                addApplicant(jobID)

        elif applyJob == '2':
            print("Application cancelled\n")

def getGradDate():
    while True:
        try:
            gradDate = input("\nEnter your graduation date in mm/dd/yyyy format: ")
            datetime.datetime.strptime(gradDate, '%m/%d/%Y')
        except ValueError as e:
            print("Please enter the date in mm/dd/yyyy format;", e)
        else:
            return gradDate

def getStartDate():
    while True:
        try:
            startDate = input("\nEnter the soonest date you can start working in mm/dd/yyyy: ")
            datetime.datetime.strptime(startDate, '%m/%d/%Y')
        except ValueError as e:
            print("Please enter the date in mm/dd/yyyy format;", e)
        else:
            return startDate

def getParagraph():
    paragraph = input("\nPlease explain why you would be a good match for this job: ")
    return paragraph

def addApplicant(jobIDno):
    applicationFile = getApplicationsFile()
    with open(applicationFile) as jsonFile:
        data = json.load(jsonFile)
        temp = data
        applicationDictionary = {  
                "graduationDate": getGradDate(),
                "startDate": getStartDate(),
                "paragraph": getParagraph()
            }
        if jobIDno in temp[getUser()]:
            print("You cannot apply to a job you've already applied to")
            return
        temp[getUser()][jobIDno] = applicationDictionary
    writeJson(data, applicationFile)