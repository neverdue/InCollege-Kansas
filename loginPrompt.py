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

    #For a new account
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
    
    #For an existing account
    else:
        exitLoop = 0

        user = userPassInput.userInput(input("Enter username: "))
        password = userPassInput.passwordInput(input("Enter password: "))

        while exitLoop != 1:
            #scanning file
            with open("users.txt", "r") as file:
                if exitLoop != 1:
                    for accounts in file:
                        accounts.split()
                        #checking username and password
                        for i in range(1):
                            if user == accounts.split()[0] and password == accounts.split()[1]:
                                exitLoop = 1
                                break
                    if exitLoop != 1:
                        print("Incorrect username / password, please try again.")
                        user = userPassInput.userInput(input("Enter username: "))
                        password = userPassInput.passwordInput(input("Enter password: "))

        print("You have successfully logged in.")
                    
login()

