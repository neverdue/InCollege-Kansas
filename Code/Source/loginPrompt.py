from Code.Source.accountCount import accountLimit
from Code.Source.accountCheck import accountExist
from Code.Source.passwordCheck import securePassword
import globalVariables

#Create a prompt that asks a user to input their username and password

#Takes user input for username and password
#Stores concatenated user and password separated by a space into a file

#Dependent on other functions each imported from their own file

def register(username, password, TESTMODE = False):
    globalVariables.addPage("register")

    if TESTMODE == True:
        fileWrite = open("users-test.txt", "a")
    else:
        fileWrite = open("users.txt", "a")

    if accountExist(username, TESTMODE) == 1:
        print("Username {} already exists, please try again.".format(username)) 
        return
    if accountLimit(TESTMODE) >= 5:
        print("All permitted accounts have been created, please come back and try later.")
        return

    while securePassword(password) != 1:
        password = input("Enter password: ")
    
    print("You have successfully registered.")

    combiUserPass = username + " " + password + "\n"
    fileWrite.write(combiUserPass)
    fileWrite.close()
    return 1

def login(username, password, TESTMODE = False):
    exitLoop = 0

    if accountExist(username, TESTMODE) != 1: 
        print("User does not exist.")
        return

    while exitLoop != 1:
        #scanning file
        if verifyCredentials(username, password, TESTMODE) != 1:
            print("Incorrect username / password, please try again.")
            username = input("Enter username: ")
            password = input("Enter password: ")
        else:
            print("You have successfully logged in.")
            exitLoop = 1

    return 1

def verifyCredentials(usernameInput, passwordInput, TESTMODE = False):
    if TESTMODE == True:
        fileOpen = open("users-test.txt", "r")
    else:
        fileOpen = open("users.txt", "r")

    with fileOpen as file:
            for accounts in file:
                if usernameInput == accounts.split()[0] and passwordInput == accounts.split()[1]:
                    return 1
    return 0
