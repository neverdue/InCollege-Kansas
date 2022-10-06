import json
from logging import lastResort
from Code.Source.dupNames import uniqueNames
from Code.Source.globalVariables import addPage, getFirst, getJobFile, getLast, getLoggedUser, removePage, printStack, logout
from Code.Source.menuOptions import about, accessibility, back, blog, brandPolicy, browseInCollege, businessSolutions, careers, cookiePolicy, copyrightNotice, copyrightPolicy, developers, directories, guestControls, helpCenter, languages, press, underConstruction, userAgreement
from Code.Source.utility import checkPages, inputValidation, printDivider, writeJson
from Code.Source.loginPrompt import signUpPage, login, register
from Code.Source.successStory import storyDisplay
from Code.Source.accountCount import accountLimit
from Code.Source.potentialConnection import find

def mainPage():
    addPage(mainPage)
    logout()
    storyDisplay()
    try:
        menuSelection = int(input("Welcome to InCollege!\n\nSelect 1 to login to an existing account\nSelect 2 to register a new account\nSelect 3 to connect to an existing user\nSelect 4 to view introduction video\nSelect 5 to view Useful Links\nSelect 6 to view InCollege Important Links\n\nSelection: "))
    except ValueError:
        print("Invalid input!")
        return

    while (menuSelection not in range(1, 7)):
        print("Invalid selection, please try again.\n")
        try:
            menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))
        except ValueError:
            print("Invalid input!")
            return

    if menuSelection == 1 and accountLimit() != 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password) == 1:
            homePage()

    elif menuSelection == 2:
        if signUpPage() == 1:
            homePage()

    elif menuSelection == 3:
        firstname = input("Enter a first name: ")
        lastname = input("Enter a last name: ")

        firstname = firstname.lower()
        lastname = lastname.lower()

        if find(firstname, lastname) == 1:
            print("They are a part of the InCollege system.\nWould you like to sign up for an existing account?\n")
            message = "Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\n"
            print(message)
            try:
                signUp = int(input("Selection: "))
            except ValueError:
                print("Invalid input!")
                return
        
            while(signUp != 1 and signUp != 2):
                print("Invalid selection, please try again.\n")
                print(message)
                try:
                    signUp = int(input("Selection: "))
                except ValueError:
                    print("Invalid input!")
                    return
            if signUp == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                firstname = input("Enter your first name: ")
                lastname = input("Enter your last name: ")
                while(uniqueNames(firstname, lastname) == 0):
                    firstname = input("Enter your first name: ")
                    lastname = input("Enter your last name: ")
                if register(username, password, firstname, lastname) == 1:
                    homePage()
            elif signUp == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login(username, password) == 1:
                    homePage()
        else:
            print("They are not yet a part of the InCollege system yet.")

    elif menuSelection == 4:
        print("Video is now playing\n\n")

    elif menuSelection == 5:
        usefulLinksMenu()

    elif menuSelection == 6:
        incollegeImpLinks()

def incollegeImpLinks():
    addPage(incollegeImpLinks)
    printStack()
    message = "Select 1 for Copyright Notice\nSelect 2 for About\nSelect 3 for Accessibility\nSelect 4 for User Agreement\nSelect 5 for Privacy Policy\nSelect 6 for Cookie Policy\nSelect 7 for Copyright Policy\nSelect 8 for Brand Policy\nSelect 9 for Languages\nSelect 10 to go back\n"
    printDivider()
    print(message)
    inputSelection = inputValidation(1, 11)

    if inputSelection == 1:
        links["Copyright Notice"]()
    elif inputSelection == 2:
        links["About"]()
    elif inputSelection == 3:
        links["Accessibility"]()
    elif inputSelection == 4:
        links["User Agreement"]()
    elif inputSelection == 5:
        links["Privacy Policy"]()
    elif inputSelection == 6:
        links["Cookie Policy"]()
    elif inputSelection == 7:
        links["Copyright Policy"]()
    elif inputSelection == 8:
        links["Brand Policy"]()
    elif inputSelection == 9:
        links["Languages"]()
    elif inputSelection == 10:
        links["Back"]()


def usefulLinksMenu():
    addPage(usefulLinksMenu)
    printStack()
    message = "Select 1 for General\nSelect 2 for Browse InCollege\nSelect 3 for Business Solutions\nSelect 4 for Directories\nSelect 5 to go back\n"
    printDivider()
    print(message)
    inputSelection = inputValidation(1, 6)

    if inputSelection == 1:
        links["General"]()
    elif inputSelection == 2:
        links["Browse InCollege"]()
    elif inputSelection == 3:
        links["Business Solutions"]()
    elif inputSelection == 4:
        links["Directories"]()
    elif inputSelection == 5:
        links["Back"]()


def general():
    addPage(general)
    printStack()
    message = "You are at the General Page!\n\n"
    message += "Select 1 for Sign Up\nSelect 2 for Help Center\nSelect 3 for About\nSelect 4 for Press\nSelect 5 for Blog\nSelect 6 for Careers\nSelect 7 for Developers\nSelect 8 to go back\n"
    printDivider()
    print(message)
    inputSelection = inputValidation(1, 9)
    
    if inputSelection == 1:
        links["Sign Up"]()
    elif inputSelection == 2:
        links["Help Center"]()
    elif inputSelection == 3:
        links["About"]()
    elif inputSelection == 4:
        links["Press"]()
    elif inputSelection == 5:
        links["Blog"]()
    elif inputSelection == 6:
        links["Careers"]()
    elif inputSelection == 7:
        links["Developers"]()
    elif inputSelection == 8:
        links["Back"]()

def privacyPolicy():
    addPage(privacyPolicy)
    printDivider()
    message = "Select 1 for Guest Controls\nSelect 2 to go back\n"
    print(message)
    inputSelection = inputValidation(1, 3)
    if inputSelection == 1:
        if links["Guest Controls"]() == -1:
            exit
    elif inputSelection == 2:
        links["Back"]()

links = {
    "mainPage": mainPage,
    "Useful Links": usefulLinksMenu,
    "InCollege Important Links": incollegeImpLinks,
    "General": general,
    "Browse InCollege": browseInCollege,
    "Business Solutions": businessSolutions,
    "Directories": directories,
    "Sign Up": signUpPage,
    "Help Center": helpCenter,
    "About": about,
    "Press": press,
    "Blog": blog,
    "Careers": careers,
    "Developers": developers,
    "Copyright Notice": copyrightNotice,
    "Accessibility": accessibility, 
    "User Agreement": userAgreement,
    "Privacy Policy": privacyPolicy,
    "Cookie Policy": cookiePolicy,
    "Copyright Policy": copyrightPolicy,
    "Brand Policy": brandPolicy,
    "Guest Controls": guestControls,
    "Languages": languages,
    "Back": back
}

# HOME PAGE
def showHomePageGreeting():
    printDivider()
    print("Welcome to InCollege!")
    print("""Please choose from one of the options below:\n1. Search for a job
2. Find someone you know\n3. Learn a new skill\n4. Useful Links\n5. InCollege Important Links\n6. Go to previously visited page\n""")

def showSkillPageGreeting():
    printDivider()
    print("""Learn and explore the skill options below!\n1. Communication\n2. Leadership\n3. Collaboration\n4. Responsibility\n5. Time Management\n
Please enter a number from 1-5.\nEnter x to return to the home page.\nEnter y to go to previously visited page.\n""")

def showConstructionMessage(message):
    printDivider()
    print("We're sorry!\n'{}' feature is still under construction.\n".format(message))

def homePage(): 
    #Add home page to page stack
    addPage(homePage)
    printStack()

    showHomePageGreeting()
    try: 
        user_choice = int(input("Enter your option (1, 2, 3, 4, 5 or 6): "))
    except:
        print("Invalid Input!") 
        return

    while user_choice not in range(1, 7):
        showHomePageGreeting()
        try:
            user_choice = int(input("Enter your option (1, 2, 3, 4, 5 or 6): "))   
        except:
            print("Invalid Input!") 
            return

    route(user_choice)
    returnToHomePage()

def route(user_choice):
    if user_choice == 1:
        jobPage()
    elif user_choice == 2:
        findSomeonePage()
    elif user_choice == 3:
        addPage(skillPage)
        showSkillPageGreeting()
        skill_choice = input("Your choice: ")
        while skill_choice != 'y' and skill_choice != 'x' and skill_choice not in [str(i) for i in range(1, 6)]:
            showSkillPageGreeting()
            skill_choice = input("Your choice: ")
        if skill_choice == 'x':
            homePage()
        elif skill_choice == 'y':
            lastPage = removePage()
            lastPage()
            # checkPages(lastPage, homePageLinks)
        else: 
            skillPage(skill_choice)
    elif user_choice == 4:
        usefulLinksMenu()
    elif user_choice == 5:
        incollegeImpLinks()
    elif user_choice == 6:
        lastPage = removePage()
        lastPage()
        # checkPages(lastPage, homePageLinks)

def returnToHomePage():
    if getLoggedUser() == None:
        return
    user_choice = input('Go back to homepage? (y/n): ')
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Please enter y for yes, n for no: ')
    if user_choice == 'y':
        homePage()
    else: 
        printDivider()
        exit

def jobPage():
    addPage(jobPage)

    message = "\n1. Post a job\n2. Home page\n3. Previous Page\n"
    print(message)
    user_choice = input("Enter your option: ")
    while user_choice != '1' and user_choice != '2' and user_choice != '3':
        print("\nInvalid input.\n" + message)
        user_choice = input("Enter your option: ")
    if user_choice == '1':
        addJobPost()
    elif user_choice == '2':
        homePage() 
    elif user_choice == '3':
        back()
        # checkPages(lastPage, homePageLinks)
    
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

def main():
    homePage()

homePageLinks = {
    "job": jobPage,
    "findSomeone": findSomeonePage,
    "learnSkill": skillPage,
    "home": homePage,
    "main": main,
    "postJob": addJobPost
}