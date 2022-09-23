from Code.Source.loginPrompt import register, login
from Code.Source.accountCount import accountLimit
from Code.Source.home_page import homePage, readJobPosts
from Code.Source.globalVariables import stackInit, addPage, userInit
import potentialConnection
import successStory
import json


def main():
    #Read in jobPosts at start up
    jobPosts = readJobPosts()

    #Initialize stack and add login page
    stackInit()
    addPage("main")

    successStory.storyDisplay()
    menuSelection = int(input("Welcome to InCollege!\n\nSelect 1 to login to an existing account\nSelect 2 to register a new account\nSelect 3 to connect to an existing user\nSelect 4 to view introduction video\n\nSelection: "))

    while (menuSelection != 1 and menuSelection != 2 and menuSelection != 3 and menuSelection != 4):
        print("Invalid selection, please try again.\n")
        menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))

    if menuSelection == 1 and accountLimit() != 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        temp = login(username, password)
        if temp == 1:
            #get logged in user's first and last name
            with open("accounts.json", "r") as json_file:
                data = json.load(json_file)
                for items in data["accounts"]:
                    tempUser = items["username"]
                    if username == tempUser:
                        firstname = items["firstName"]
                        lastname = items["lastName"]
            #set user variable
            userInit(username, firstname, lastname)
            homePage()

    elif menuSelection == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        temp = register(username, password, firstname, lastname)
        if temp == 1:
            userInit(username, firstname, lastname)
            homePage()

    elif menuSelection == 3:
        firstname = input("Enter a first name: ")
        lastname = input("Enter a last name: ")

        firstname = firstname.lower()
        lastname = lastname.lower()

        if potentialConnection.find(firstname, lastname) == 1:
            print("They are a part of the InCollege system.\nWould you like to sign up for an existing account?\n")
            signUp = int(input("Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\nSelection: "))

            while(signUp != 1 and signUp != 2):
                print("Invalid selection, please try again.\n")
                signUp = int(input("Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\nSelection: "))
            if signUp == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                firstname = input("Enter your first name: ")
                lastname = input("Enter your last name: ")
                temp = register(username, password, firstname, lastname)
                if temp == 1:
                    (username, firstname, lastname)
                    homePage()
            elif signUp == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                temp = login(username, password)
                if temp == 1:
                    #get logged in user's first and last name
                    with open("accounts.json", "r") as json_file:
                        data = json.load(json_file)
                        for items in data["accounts"]:
                            tempUser = items["username"]
                            if username == tempUser:
                                firstname = items["firstName"]
                                lastname = items["lastName"]
                    #set user variable
                    userInit(username, firstname, lastname)
                    homePage()
        else:
            print("They are not yet a part of the InCollege system yet.")

    elif menuSelection == 4:
        print("Video is now playing\n\n")
        main()

if __name__ == "__main__":
    main()