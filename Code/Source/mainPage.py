from Code.Source.menu import homePage, incollegeImpLinks, usefulLinksMenu
from Code.Source.utility import endProgram, uniqueNames, storyDisplay, accountLimit, find, inputValidation
from Code.Source.globalVariables import addPage, logout, getTimer
from Code.Source.loginPrompt import signUpPage, login, register
import time

def mainPage():
    addPage(mainPage)
    logout()
    storyDisplay()
    timer = getTimer()
    time.sleep(timer)
    
    print("Welcome to InCollege!\n\nSelect 1 to login to an existing account\nSelect 2 to register a new account\nSelect 3 to connect to an existing user\nSelect 4 to view introduction video\nSelect 5 to view Useful Links\nSelect 6 to view InCollege Important Links\n")
    menuSelection = inputValidation(1, 6)

    if menuSelection == '1' and accountLimit() != 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password) == 1:
            homePage()

    elif menuSelection == '2':
        if signUpPage() == 1:
            homePage()

    elif menuSelection == '3':
        firstname = input("Enter a first name: ")
        lastname = input("Enter a last name: ")

        firstname = firstname.lower()
        lastname = lastname.lower()

        if find(firstname, lastname) == 1:
            print("They are a part of the InCollege system.\nWould you like to sign up for an existing account?\n")
            message = "Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\n"
            print(message)
            signUp = inputValidation(1, 3)
                
            if signUp == '1':
                if signUpPage() == 1:
                    homePage()
            elif signUp == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login(username, password) == 1:
                    homePage()
        else:
            print("They are not yet a part of the InCollege system yet.")

    elif menuSelection == '4':
        print("Video is now playing\n\n")

    elif menuSelection == '5':
        usefulLinksMenu()

    elif menuSelection == '6':
        incollegeImpLinks()