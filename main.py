from Code.Source.loginPrompt import register, login
from Code.Source.accountCount import accountLimit
from Code.Source.home_page import homePage, readJobPosts
from Code.Source.globalVariables import dataFileInit, getDataFile, stackInit, addPage
from Code.Source.dupNames import uniqueNames
from Code.Source.successStory import storyDisplay
from Code.Source.potentialConnection import find
import json


def main():
    dataFileInit()
    #Read in jobPosts at start up
    jobPosts = readJobPosts()

    #Initialize stack and add login page
    stackInit()
    addPage("main")

    storyDisplay()
    try:
        menuSelection = int(input("Welcome to InCollege!\n\nSelect 1 to login to an existing account\nSelect 2 to register a new account\nSelect 3 to connect to an existing user\nSelect 4 to view introduction video\n\nSelection: "))
    except ValueError:
        print("Invalid input!")
        return

    while (menuSelection not in range(1, 5)):
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
        username = input("Enter username: ")
        password = input("Enter password: ")
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        while(uniqueNames(firstname, lastname) == 0):
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
        if register(username, password, firstname, lastname) == 1:
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

if __name__ == "__main__":
    main()