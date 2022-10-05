from Code.Source.home_page import checkPages, printDivider
from Code.Source.globalVariables import addPage, removePage, printStack
from Code.Source.loginPrompt import signUpPage

def linksNotSignedIn():
    # usefulLinksMenu
    # Incollege important links
    pass

def linksSignedIn():
    # homePage
    # usefulLinksMenu
    # Incollege important links
    pass

def usefulLinksMenu():
    addPage("Useful Links")
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
    addPage("General")
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
    
def underConstruction(page):
    addPage(page)
    printDivider()
    print("Under construction")
    printDivider()
    goBackOption()

def helpCenter():
    addPage("Help Center")
    printDivider()
    print("We're here to help")
    printDivider()
    goBackOption()

def about():
    addPage("About")
    printDivider()
    print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
    printDivider()
    goBackOption()

def press():
    addPage("Press")
    printDivider()
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    printDivider()
    goBackOption()

def goBackOption():
    message = "Select 1 to go back\n"
    print(message)
    inputSelection = inputValidation(1, 2)
    if inputSelection == 1:
        links["Back"]()

def back():
    lastPage = removePage()
    checkPages(lastPage, links)

def inputValidation(left, right):
    try:
        inputSelection = int(input("Selection: "))
    except ValueError:
        print("Invalid input!")
        return
    while (inputSelection not in range(left, right)):
        print("Invalid selection, please try again.\n")
        try:
            inputSelection = int(input("Selection: "))
        except ValueError:
            print("Invalid input!")
            return
    return inputSelection

links = {
    "Useful Links": usefulLinksMenu,
    "General": general,
    "Browse InCollege": lambda: underConstruction("Browse InCollege"),
    "Business Solutions": lambda: underConstruction("Business Solutions"),
    "Directories": lambda: underConstruction("Directories"),
    "Sign Up": signUpPage,
    "Help Center": helpCenter,
    "About": about,
    "Press": press,
    "Blog": lambda: underConstruction("Blog"),
    "Careers": lambda: underConstruction("Careers"),
    "Developers": lambda: underConstruction("Developers"),
    "Back": back
}