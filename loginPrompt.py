import accountCount
import accountCheck
import passwordCheck
import json
import writeJson
import potentialConnection

#import printJson

#Create a prompt that asks a user to input their username and password

#Takes user input for username and password
#Stores concatenated user and password separated by a space into a file

#Dependent on other functions each imported from their own file

#################################################################
# 9/22/22 altered functions to also take first+last name
# replaced account text file with json file

# QUESTION: When we create an account, the system needs to check if there are 5 or more accounts.
#           When it does check during account creation, it still requests first name and last name
#           The issue that occurs that its wasted time if there are 5 accounts but on the 6th, the system still asks for first + last name
#           The funtionality still works, but it doesn't make sense for it still to ask for first and last name during the 6th account checking
#           Now this may be fine since Epic2 doesn't specify if this is an issue or not

# QUESTION: Should we convert all user input to lower/upper case for ease of checking in other functions?
#################################################################


def main():
    menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelect 3 to connect to an existing user\nSelection: "))

    while (menuSelection != 1 and menuSelection != 2 and menuSelection != 3):
        print("Invalid selection, please try again.\n")
        menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))

    if menuSelection == 1 and accountCount.accountLimit() != 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username, password)

    elif menuSelection == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        firstname = input("Enter your first name: ")
        lastname = input("Enter your last name: ")
        register(username, password, firstname, lastname)

    elif menuSelection == 3:
        firstname = input("Enter a first name: ")
        lastname = input("Enter a last name: ")

        firstname = firstname.lower()
        lastname = lastname.lower()

        if potentialConnection.find(firstname, lastname) == 1:
            print("They are a part of the InCollege system.\nWould you like to sign up for an existing account?")
            signUp = int(input("Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\nSelection: "))

            while(signUp != 1 and signUp != 2):
                print("Invalid selection, please try again.\n")
                signUp = int(input("Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\nSelection: "))
            if signUp == 1:
                username = input("Enter username: ")
                password = input("Enter password: ")
                firstname = input("Enter your first name: ")
                lastname = input("Enter your last name: ")
                register(username, password, firstname, lastname)
            elif signUp == 2:
                username = input("Enter username: ")
                password = input("Enter password: ")
                login(username, password)
        else:
            print("They are not yet a part of the InCollege system yet.")

    

def register(username, password, first, last): 
    if accountCheck.accountExist(username) == 1:
        print("Username {} already exists, please try again.".format(username)) 
        return
    if accountCount.accountLimit() >= 5:
        print("All permitted accounts have been created, please come back and try later.")
        return

    while passwordCheck.securePassword(password) != 1:
        password = input("Enter password: ")
    
    print("You have successfully registered.")

    #Adding credentials + names to json
    with open("accounts.json") as json_file:
        data = json.load(json_file)
        temp = data["accounts"]
        newData = {"username": username, "password" : password, "firstName" : first, "lastName" : last}
        temp.append(newData)

    writeJson.wJson(data)
    return 1

def login(username, password):
    exitLoop = 0
    if accountCheck.accountExist(username) != 1: 
        print("User does not exist.")
        return

    while exitLoop != 1:
        #scanning file
        if verifyCredentials(username, password) != 1:
            print("Incorrect username / password, please try again.")
            username = input("Enter username: ")
            password = input("Enter password: ")
        else:
            print("You have successfully logged in.")
            exitLoop = 1
    return 1

def verifyCredentials(usernameInput, passwordInput):
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            password = items["password"]
            if usernameInput == user and passwordInput == password:
                return 1
    return 0

if __name__ == "__main__":
    main()

