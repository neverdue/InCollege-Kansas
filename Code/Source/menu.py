from Code.Source.homePageOptions import findSomeonePage, jobPage, returnToHomePage, searchUsers, showHomePageGreeting, showMyNetwork, showSkillPageGreeting, skillPage, viewIncomingRequests, viewOutgoingRequests, createProfile, showProfile, hasProfile, displayProfile, getProfile
from Code.Source.globalVariables import addPage, getIncomingRequests, getLoggedUser, removePage, getUser
from Code.Source.menuOptions import about, accessibility, back, brandPolicy, browseInCollege, businessSolutions, cookiePolicy, copyrightNotice, copyrightPolicy, directories, general, languages, privacyPolicy, userAgreement
from Code.Source.utility import endProgram, inputValidation, printDivider

def incollegeImpLinks():
    addPage(incollegeImpLinks)
    message = "Select 1 for Copyright Notice\nSelect 2 for About\nSelect 3 for Accessibility\nSelect 4 for User Agreement\nSelect 5 for Privacy Policy\nSelect 6 for Cookie Policy\nSelect 7 for Copyright Policy\nSelect 8 for Brand Policy\nSelect 9 for Languages\nSelect 10 to go back\n"
    printDivider()
    print(message)
    inputSelection = inputValidation(1, 11)

    if inputSelection == 1:
        copyrightNotice()
    elif inputSelection == 2:
        about()
    elif inputSelection == 3:
        accessibility()
    elif inputSelection == 4:
        userAgreement()
    elif inputSelection == 5:
        privacyPolicy()
    elif inputSelection == 6:
        cookiePolicy()
    elif inputSelection == 7:
        copyrightPolicy()
    elif inputSelection == 8:
        brandPolicy()
    elif inputSelection == 9:
        languages()
    elif inputSelection == 10:
        back()

def usefulLinksMenu():
    addPage(usefulLinksMenu)
    message = "Select 1 for General\nSelect 2 for Browse InCollege\nSelect 3 for Business Solutions\nSelect 4 for Directories\nSelect 5 to go back\n"
    printDivider()
    print(message)
    inputSelection = inputValidation(1, 6)

    if inputSelection == 1:
        if general() == "homePage":
            homePage()
    elif inputSelection == 2:
        browseInCollege()
    elif inputSelection == 3:
        businessSolutions()
    elif inputSelection == 4:
        directories()
    elif inputSelection == 5:
        back()

# HOME PAGE
def homePage(): 
    #Add home page to page stack

    addPage(homePage)

    incomingRequests = getIncomingRequests()
    if len(incomingRequests) > 0:
        printDivider()
        if len(incomingRequests) == 1:
            print("You have " + str(len(incomingRequests)) + " incoming friend request!")
        else:
            print("You have " + str(len(incomingRequests)) + " incoming friend requests!")

    showHomePageGreeting()
    print("Enter your option (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, or 12).")
    user_choice = inputValidation(1, 13)

    route(user_choice)
    if returnToHomePage() == "homePage":
        homePage()

def route(user_choice):
    if user_choice == 1:
        if jobPage() == "homePage":
            homePage()
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
        else: 
            skillPage(skill_choice)
    elif user_choice == 4:
        usefulLinksMenu()
    elif user_choice == 5:
        incollegeImpLinks()
    elif user_choice == 6:
        searchUsers()
    elif user_choice == 7:
        viewIncomingRequests()
    elif user_choice == 8:
        viewOutgoingRequests()
    elif user_choice == 9:
        showMyNetwork()
    elif user_choice == 10:
        showProfile() if hasProfile() else createProfile()
    elif user_choice == 11:
         displayProfile(getProfile(getUser()) ,(getLoggedUser()["firstName"] + " " + getLoggedUser()["lastName"]))
    elif user_choice == 12:
        back()