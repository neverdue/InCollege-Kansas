from getpass import getuser
import json
import datetime

from pyparsing import empty
from Code.Source.globalVariables import addPage, getIfSubcribed, getLastLogin, getMessageFile, removePage, getApplicationsFile, getFirst, getFriendsList, getIncomingRequests, getDataFile, getJobFile, getLast, getOutgoingRequests, getUser, getUserProfile, setProfileInfo, setExperienceInfo, getExperienceCount, setEducationInfo, getEducationCount, getLoggedUser
from Code.Source.globalVariables import PROFILE_KEYS, EXPERIENCE_KEYS, EDUCATION_KEYS
from Code.Source.menuOptions import back, goBackOption
from Code.Source.utility import accountExist, accountLimit, addToFriendsList, createRequest, endProgram, getJobDict, getUserFriendList, inputValidation, checkLength, isInFriendslist, retrieveUser, printDivider, removeFromFriendsList, removeRequest, searchFilter, viewUser, writeJson, wJson, isDate, isDigit, continueInput

MAX_JOBS = 10 
MAX_EXPERIENCE = 3 

def showHomePageGreeting():
    printDivider()
    print("Welcome to InCollege!")
    print("""Please choose from one of the options below:\n1. Search for a Job\n2. Find Someone You Know\n3. Learn a New Skill\n4. Useful Links\n5. InCollege Important Links\n6. Search Users
7. See Incoming Friend Requests\n8. See Outgoing Friend Requests\n9. Show My Network\n10. Your Profile\n11. View Message Inbox\n12. Go to Previously Visited Page\n""")

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
    printDivider()

    deletedJobTitles = getDeletedApplications(getUser())
    if deletedJobTitles:
        [print(f'Job titled "{title}" you have applied for was deleted!\n') for title in deletedJobTitles]

    print("1. Post a job\n2. See your job posts\n3. See saved jobs\n4. See applied jobs\n5. See unapplied jobs\n6. See all job posts\n7. Home page\n")
    user_choice = inputValidation(1, 7)

    if user_choice == '1':
        return addJobPost()
    elif user_choice == '2':
        return getYourJobs()
    elif user_choice == '3':
        return getSavedJobs()
    elif user_choice == '4':
        return getAppliedJobs()
    elif user_choice == '5':
        return getUnappliedJobs()
    elif user_choice == '6':
        return showAllJobs() 
    elif user_choice == '7':
        back()

def addJobPost():
    fileName = getJobFile()

    #Checks if already 10 job posts
    with open (fileName) as jsonFile:
        data = json.load(jsonFile)
        temp1 = data["numPosts"]
        if temp1 >= MAX_JOBS:
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

    id = 1
    for item in data["jobPosts"]:
        if id == int(item["id"]): 
            id += 1
    
    jobDictionary = {
        "id" : str(id), ##
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
    user_choice = inputValidation(1, 4)
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
        userInput = int(inputValidation(2, 8))
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
            print("\nEnter a paragraph about yourself: ", end='')
        else: 
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
    index = int(inputValidation(1, count)) - 1
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

# Compares ID from jobPosts to ID in applications. Used to find existing applicants
def compareApplicationID(jsonObj):
    count = 0
    for items in jsonObj["jobPosts"]:
        jobID = items["id"]
        with open(getApplicationsFile()) as json_file2:
            data2 = json.load(json_file2)
            temp = data2["applications"]
            if jobID in temp[getUser()]:
                count+=1
                print(str(count) + ". " + items["Title"] +  " (applied)")
                continue
            elif jobID in getSavedJobIDs():
                count+=1
                print(str(count) + ". " + items["Title"] +  " (saved)")
            elif getUser() not in temp or jobID not in temp[getUser()]:
                count+=1
                print(str(count) + ". " + items["Title"])
    return count

# Shows list of posted jobs from json jobs file
def showAllJobs():
    addPage(showAllJobs)
    printDivider()
    filename = getJobFile()
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        length = compareApplicationID(data)
        print("\nSelect {}{} to view job posting.\nSelect {} to go to previous page.\n".format('1-' if length > 1 else '', length, length+1))
        userInput = inputValidation(1, length+1)
        if userInput == str(length+1): back()

        # Showing details of the job selected
        jobID = data["jobPosts"][int(userInput)-1]["id"]
        for item in data["jobPosts"]:
            if item["id"] == jobID:
                displayJob(item)

        jobActionMenu(jobID)
        return previousOrHomePage()

def jobActionMenu(jobID, jobMessage=''): 
    unsave = True if jobID in getSavedJobIDs() else False
    print("\n1. Apply for this job\n2. {} this job\n3. Go to previous page\n4. Home page\n".format("Unsave" if unsave else "Save"))
    userInput = inputValidation(1, 4)
    if userInput == '1':
        # Checking if the applicant is also the poster
        fullName = getFirst() + ' ' + getLast() 
        jobPost = [jobPost for jobPost in readJobPosts() if jobID == jobPost["id"]][0]
        if jobPost["Name"] == fullName:
            print("\nYou can't apply to a job you've posted.")
        # Writing info about applicant to applications json
        else:
            addApplicant(jobID)
    elif userInput == '2':
        unappliedJobIDs = [job["id"] for job in unappliedJobs()]
        if jobID not in unappliedJobIDs:
            print("\nYou can't save a job you've posted.")
        else:
            saveJobPost(jobID, unsave)
    elif userInput == '3':
        back()
    else:
        removePage()
        return "homePage"
    removePage()
    if jobMessage != '':
        return getSavedJobs() if "saved" in jobMessage else getUnappliedJobs()
    showAllJobs()

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
        temp = data["applications"]
        if getUser() not in temp:
            temp[getUser()] = {}
            writeJson(data, applicationFile)
        elif jobIDno in temp[getUser()]:
            print("You cannot apply to a job you've already applied to")
            return
        applicationDictionary = {  
            "Title": getJobDict(jobIDno)["Title"],
            "graduationDate": getGradDate(),
            "startDate": getStartDate(),
            "paragraph": getParagraph(),
            "WhenApplied": datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        }
        temp[getUser()][jobIDno] = applicationDictionary
    writeJson(data, applicationFile)

def showFilteredJobs(jobPosts, jobMessage, errMessage):
    printDivider()
    if not jobPosts:
        print(errMessage)
        return previousOrHomePage()
    try: 
        userInput = displayJobPosts(jobPosts, jobMessage)
        jobDict = jobPosts[userInput]
    except IndexError:
        return "homePage"
    displayJob(jobDict)

    if "Your posted jobs" in jobMessage:
        return deleteJobMenu(jobDict)
    elif "have applied" in jobMessage:
        return previousOrHomePage()
    elif "saved" in jobMessage:
        return jobActionMenu(jobDict["id"], "saved")
    else: return jobActionMenu(jobDict["id"], "unapplied")
    
def getYourJobs():
    addPage(getYourJobs)
    jobPosts = [jobPost for jobPost in readJobPosts() if jobPost["Name"] == getFirst() + ' ' + getLast()]
    jobMessage, errMessage = "Your posted jobs:\n", "You don't have any job posted. Please post a job!"
    return showFilteredJobs(jobPosts, jobMessage, errMessage)

def getAppliedJobs():
    addPage(getAppliedJobs)
    appliedJobIDs = getJobApplications(getUser())
    jobPosts = [jobPost for jobPost in readJobPosts() if jobPost["id"] in appliedJobIDs]
    jobMessage, errMessage = "Jobs you have applied for:\n", "You haven't applied to any jobs yet!"
    return showFilteredJobs(jobPosts, jobMessage, errMessage)

def unappliedJobs():
    appliedJobIDs = getJobApplications(getUser())
    fullName = getFirst() + ' ' + getLast()
    return [jobPost for jobPost in readJobPosts() if (not appliedJobIDs or jobPost["id"] not in appliedJobIDs) and jobPost["Name"] != fullName] 

def getUnappliedJobs():
    addPage(getUnappliedJobs)
    jobPosts = unappliedJobs()
    jobMessage, errMessage = "Jobs you have not applied for:\n", "You have applied to all applicable jobs!"
    return showFilteredJobs(jobPosts, jobMessage, errMessage)

def getSavedJobs():
    addPage(getSavedJobs)
    jobPosts = [jobPost for jobPost in readJobPosts() if jobPost["id"] in getSavedJobIDs()]
    jobMessage, errMessage = "Jobs you have saved:\n", "You haven't saved any jobs yet!"
    return showFilteredJobs(jobPosts, jobMessage, errMessage)

def displayJob(jobDict):
    addPage(displayJob)
    printDivider()
    [print(f"{key}: {jobDict[key]}") for key in jobDict if key != "id" and key != "Name"]

def displayJobPosts(jobPosts, message=''):
    print(message)
    [print("{}. {}{}".format(count, job["Title"], mark(job["id"], message))) for count, job in enumerate(jobPosts, start=1)]
    length = len(jobPosts)
    print("\nSelect {}{} to view job posting.\nSelect {} to go to previous page.\n".format('1-' if length > 1 else '', length, length+1))
    userInput = inputValidation(1, length+1)
    if userInput == str(length+1):
        back()
    return int(userInput) - 1 # return the index to the list of jobPosts
     
def mark(jobID, message):
    if "have not applied" in message:
        return " (saved)" if jobID in getSavedJobIDs() else ""
    return "" 

def deleteJobMenu(jobDict): 
    print("\nSelect 1 if you want to delete your job post.\nSelect 2 to go to previous page.\n")
    userInput = inputValidation(1, 2)
    if userInput == '1':
        deleteJobPost(jobDict["id"])
        deleteApplications(jobDict["id"], jobDict["Title"])
        printDivider()
        print("Your job post is successfully deleted!")
    back()
    
def getJobApplications(username):
    fileName = getApplicationsFile()
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
        return data["applications"][username] if username in data["applications"] else [] 

def saveJobPost(jobID, unsave=False):
    fileName = getApplicationsFile()
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
        if getUser() not in data["saved"]: data["saved"][getUser()] = [] 
        savedData = data["saved"][getUser()] 
        if unsave: 
            savedData.remove(jobID)
            if not savedData:
                del data["saved"][getUser()]
            print("\nThis job is unsaved!")
        else:
            savedData.append(jobID)
            print("\nThis job is saved!")
    writeJson(data, fileName)

def getSavedJobIDs():
    fileName = getApplicationsFile()
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
        return data["saved"][getUser()] if getUser() in data["saved"] else [] 

def deleteJobPost(jobID):
    fileName = getJobFile()
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
        jobPosts = data["jobPosts"]
        jobPosts[:] = [jobPost for jobPost in jobPosts if jobPost["id"] != jobID] 
        data["numPosts"] -= 1
    writeJson(data, fileName)
        
def deleteApplications(jobID, jobTitle):
    fileName = getApplicationsFile()
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
        deletedApps = data["deletedApplications"]
        applications = data["applications"]
        for applicant, application in applications.items():
            for id in list(application):
                if id == jobID: 
                    if applicant not in deletedApps:
                        deletedApps[applicant] = [] 
                    deletedApps[applicant].append(jobTitle)
                    del application[id]
    writeJson(data, fileName) 

def getDeletedApplications(username):
    fileName = getApplicationsFile()
    with open(fileName) as jsonFile:
        data = json.load(jsonFile)
        if username in data["deletedApplications"]:
            deletedJobTitles = data["deletedApplications"][username]
            del data["deletedApplications"][username]
            writeJson(data, fileName)
        else:
            deletedJobTitles = [] 
    return deletedJobTitles

def previousOrHomePage():
    print("\n1. Previous page\n2. Home page\n")
    userInput = inputValidation(1, 2)
    if userInput == '1':
        back()
    else: 
        removePage()
        return "homePage"

#Implement message feature
def messageInbox():
    addPage(messageInbox)
    printDivider()
    print("-----I N B O X------\n\n")

    #If no other users in system
    if accountLimit == 1:
        print("There are no other users to message")
        return

    subStatus = getIfSubcribed()
    userChoice = input("Would you like to message a new user (1) or view, send, or delete your current messages (2)?: ")

    #If messaging user, check subscription status to see who they can send a message to
    if userChoice == '1':
        #If plus user
        if subStatus == True:
            print("\nBelow are the users in the system\n")
            #Prints all users in system
            dataFile = getDataFile()
            with open(dataFile) as json_file:
                data = json.load(json_file)
                for users in data["accounts"]:
                    if getUser() == users["username"]:
                        continue
                    else:
                        print(users["username"])

            mesUser = input("\nPlease input the username of the user you want to message: ")

            #Loops until valid username
            while accountExist(mesUser) == 0:
                mesUser = input("Invalid username. Please input the username of the user you want to message: ")

            # Sends and receives messages at the same time
            receiveMessage(sendMessage(mesUser, subStatus), mesUser)
            

        #Standard User
        elif subStatus == False:
            friendCount = 1
            for friends in getFriendsList():
                print(str(friendCount) + ") " + friends)
                friendCount+=1
            mesUser = input("\nPlease input the username of the user you want to message: ")

            while accountExist(mesUser) == 0:
                mesUser = input("Invalid username. Please input the username of the user you want to message: ")
            #Checks if user is in friends list OR if they have messages from them already
            ifFriend = isInFriendslist(mesUser)

            if ifFriend == True: 
                # Sends and receives messages at the same time
                receiveMessage(sendMessage(mesUser, subStatus), mesUser)
                print("Done!")
            else:
                print("I'm sorry, you are not friends with that person")

        else: 
            print("Error occurred")

    # Make user choose messages to view then decide to reply, delete, or go back
    elif userChoice == '2':
        recipient = showSendersSelection()
        if recipient == 0:
            return

        print("Enter (1) to reply to this user, (2) to delete a specific message, or (3) to go back:\n")
        userAction = inputValidation(1, 3)

        if userAction == '1':
            # Fill outgoing inbox and incoming inbox at the same time
            receiveMessage(sendMessage(recipient, subStatus), recipient)
        elif userAction == '2':
            # Check if there are entries in the inbox
            if messageCount(recipient) >= 1:
                print("Which message would you like to delete?")
                messageIndexDelete = inputValidation(1, messageCount(recipient))
                deleteMessage(recipient, messageIndexDelete)
    
    return

# Adds to outgoing field in inbox json
def sendMessage(recipient, subStatus):
    # Sanity check for testing and epic requirements (shouldn't ever be reached)
    if (recipient not in getFriendsList() and subStatus != True) or (recipient == getUser()):
        print("I'm sorry, you are not friends with that person")
        return 0
    msg = input("Enter the message you want to send to {}: ".format(recipient))
    messageFile = getMessageFile()
    with open(messageFile) as json_file:
        data = json.load(json_file)
        temp = data["outgoing"]
        # If sender not in json, add them and the recipient
        if getUser() not in temp:
            temp[getUser()] = {}
            writeJson(data, messageFile)
            temp[getUser()][recipient] = []
            writeJson(data, messageFile)
        # If sender is in json, add a new recipient to outgoing
        elif recipient not in temp[getUser()]:
            temp[getUser()][recipient] = []
            writeJson(data, messageFile)
        # Add message to list of messages
        temp[getUser()][recipient].append(msg)
    writeJson(data, messageFile)
    return msg

# Adds to incoming field in inbox json
def receiveMessage(sentMsg, recipient):
    # sentMsg is the return value of sendMessage(). Returned 0 if the person they want to send to
    # is not in their friend list or if the subbed user tries to send to themselves
    if sentMsg == 0: return
    messageFile = getMessageFile()
    with open(messageFile) as json_file:
        data = json.load(json_file)
        temp = data["incoming"]
        # If recipient not in json, add them and the sender
        if recipient not in temp:
            temp[recipient] = {}
            writeJson(data, messageFile)
            temp[recipient][getUser()] = []
            writeJson(data, messageFile)
        # If there already recipient, add a new sender field to incoming
        elif getUser() not in temp[recipient]:
            temp[recipient][getUser()] = []
            writeJson(data, messageFile)
        # Add message to list of messages
        temp[recipient][getUser()].append(sentMsg)
    writeJson(data, messageFile)
    return

# Returns a list of people who are sending the user a message
def getIncoming():
    senders = []
    messageFile = getMessageFile()
    with open(messageFile) as json_file:
        data = json.load(json_file)
        temp = data["incoming"]
        if getUser() in temp:
            for items in temp[getUser()]:
                senders.append(items)
    return senders

# Return 1 if there are awaiting messages otherwise return 0
def messageNotification():
    if getIncoming():
        printDivider()
        senders = getIncoming()
        x = "You have messages from "
        # Only 1 sender
        if len(senders) == 1:
            print(x + senders[0] + "!")
        # Multiple senders
        else:
            for items in range(0,len(senders)-1):
                x += senders[items] + ", "
            print(x + "and " + senders[-1] + "!")
        return 1
    else:
        return 0

# Almost the same exact function as displayIncomingMessages() but does not print. Returns number of messages from a user
# Used to find how many messages there are from a certain sender
def messageCount(sender):
    messageFile = getMessageFile()
    count = 1
    with open(messageFile) as json_file:
        data = json.load(json_file)
        # First if branch shouldn't ever be reached since there's another safe check in the main messageBox() function
        if getUser() not in data["incoming"]:
            print("Error: You have no messages")
            return 0
        for items in data["incoming"][getUser()][sender]:
            count+=1
    return count

# Used in conjunction with showSenderSelection to show senders AND their messages
def displayIncomingMessages(sender):
    messageFile = getMessageFile()
    count = 1
    with open(messageFile) as json_file:
        data = json.load(json_file)
        for items in data["incoming"][getUser()][sender]:
            print(str(count) + ") ", items)
            count+=1
    print("\n")

# Shows list of people trying to send to the user and inquires user who they want to interact with
# Then shows list of messages from that user they want to interact with
# Uses displayIncomingMessages() to accomplish ^
# Returns the user they interacted with
def showSendersSelection():
    if len(getIncoming()) >= 1:
        # Choosing which user to read messages from
        print("Which user's messages would you like to view?")
        printDivider()
        senderChoices = getIncoming()
        for items in senderChoices:
            print(items)
        senderSelection = input("\nSelect a username: ")
        if senderSelection == -1:
            endProgram()
        printDivider()

        # Validating input 
        while senderSelection not in senderChoices:
            printDivider()
            print("Invalid input!")
            print("Which user's messages would you like to view?")
            for items in senderChoices:
                print(items)
            senderSelection = input("\nSelect a username: ")
            if senderSelection == -1:
                endProgram()
        
        displayIncomingMessages(senderSelection)
        return senderSelection
    else:
        print("You have no incoming messages.")
        return 0
        
# Deletes from incoming, but does not delete from outgoing
def deleteMessage(senderName, msgIndex):
    if len(getIncoming()) <= 0:
        print("Error: Can't delete non-existent messages")
        return
    messageFile = getMessageFile()
    with open(messageFile) as json_file:
        data = json.load(json_file)
        data["incoming"][getUser()][senderName].pop(int(msgIndex)-1)
    writeJson(data, messageFile)

def deletedJobNotification():
    myApplications = getJobApplications(getUser())
    if len(myApplications) == 0:
        return
    allJobs = [job["id"] for job in readJobPosts()]
    for jobID, application in myApplications.items():
        if jobID not in allJobs:
            printDivider()
            print("A job that you applied for has been deleted, Job Title: " + application["Title"])
            printDivider()

def reminderToApplyNotification():
    if len(getJobApplications(getUser())) == 0:
        return
    lastApplicationTime = max([datetime.datetime.strptime(application["WhenApplied"], "%m/%d/%Y %H:%M:%S") for application in getJobApplications(getUser()).values()])
    if (datetime.datetime.now() - lastApplicationTime).days > 7:
        printDivider()
        print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
        printDivider()

def newStudentsNotification():
    newStudents = []
    with open(getDataFile()) as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            if datetime.datetime.strptime(items["registrationTime"], "%m/%d/%Y %H:%M:%S")  > datetime.datetime.strptime(getLastLogin(), "%m/%d/%Y %H:%M:%S") and items["username"] != getUser():
                newStudents.append(items)
    if len(newStudents) > 0:
        printDivider()
        for student in newStudents:
            print("{} {} has joined InCollege".format(student["firstName"], student["lastName"]))
        printDivider()
    
    # set the lastLogin time to now
    with open(getDataFile(), "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            tempUser = items["username"]
            if getUser() == tempUser:
                items["lastLogin"] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    wJson(data, getDataFile())