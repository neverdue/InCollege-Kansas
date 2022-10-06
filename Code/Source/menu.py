from Code.Source.homePageOptions import findSomeonePage, jobPage, returnToHomePage, showHomePageGreeting, showSkillPageGreeting, skillPage
from Code.Source.globalVariables import addPage, removePage, printStack
from Code.Source.menuOptions import about, accessibility, back, brandPolicy, browseInCollege, businessSolutions, cookiePolicy, copyrightNotice, copyrightPolicy, directories, general, languages, privacyPolicy, userAgreement
from Code.Source.utility import inputValidation, printDivider

def incollegeImpLinks():
    addPage(incollegeImpLinks)
    printStack()
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
    printStack()
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
        back()