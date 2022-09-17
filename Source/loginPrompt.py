import Source.accountCount as accountCount
import Source.accountCheck as accountCheck
import Source.passwordCheck as passwordCheck

#Create a prompt that asks a user to input their username and password

#Takes user input for username and password
#Stores concatenated user and password separated by a space into a file

#Dependent on other functions each imported from their own file

def main():
    fileWrite = open("users.txt", "a")
    menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))

    while (menuSelection != 1 and menuSelection != 2):
        print("Invalid selection, please try again.\n")
        menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))

    if menuSelection == 1 and accountCount.accountLimit() != 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        login(username, password)
    elif menuSelection == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        register(username, password)
    
    fileWrite.close()

def register(username, password):
    fileWrite = open("users.txt", "a")

    if accountCheck.accountExist(username) == 1: 
        return
    if accountCount.accountLimit() >= 5:
        print("All permitted accounts have been created, please come back and try later.")
        return

    while passwordCheck.securePassword(password) != 1:
        password = input("Enter password: ")
    
    print("You have successfully registered.")

    combiUserPass = username + " " + password + "\n"
    fileWrite.write(combiUserPass)
    fileWrite.close()
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
    with open("users.txt", "r") as file:
        for accounts in file:
            if usernameInput == accounts.split()[0] and passwordInput == accounts.split()[1]:
                return 1
    return 0

if __name__ == "__main__":
    main()

