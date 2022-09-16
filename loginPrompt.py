import accountCount
import accountCheck
import passwordCheck
import userPassInput

#Create a prompt that asks a user to input their username and password

#Takes user input for username and password
#Stores concatenated user and password separated by a space into a file

#Dependent on other functions each imported from their own file

def login():
    fileWrite = open("users.txt", "a")

    loginSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))

    #For an existing account
    if loginSelection != 1:
        user = userPassInput.userInput(input("Enter username: "))

        if accountCheck.accountExist(user) == 1: return
        if accountCount.accountLimit() >= 5:
            print("All permitted accounts have been created, please come back and try later.")
            return

        password = input("Enter password: ")
        while passwordCheck.securePassword(password) != 1:
            password = userPassInput.passwordInput(input("Enter password: "))

        combiUserPass = user + " " + password + "\n"
        fileWrite.write(combiUserPass)
        fileWrite.close()
    
    #For a new account creation
    else:
        exitLoop = 0
        fileOpen = open("users.txt", "r")

        user = input("Enter username: ")
        password = input("Enter password: ")
        
        while exitLoop != 1:
            for elements in fileOpen:
                users = elements.split()
                for names in range(len(users)):
                    if(user != users[0] and password != users[1]):
                        print("Incorrect username / password, please try again.")
                        user = input("Enter username: ")
                        password = input("Enter password: ")
                    else:
                        exitLoop = 1
                        break

        fileOpen.close()
        print("You have successfully logged in.")
                    
login()

