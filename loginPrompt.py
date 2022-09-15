import accountCount
import accountCheck
import passwordCheck

#Create a prompt that asks a user to input their username and password

#takes user input for username and password
#stores concatenated user and password separated by a space into a file

#dependent on 3 functions each imported from their own file

def login():
    fileWrite = open("users.txt", "a")

    user = input("Enter username: ")

    if accountCheck.accountExist(user) == 1: return
    if accountCount.accountLimit() >= 5:
        print("All permitted accounts have been created, please come back and try later.")
        return

    password = input("Enter password: ")
    while passwordCheck.securePassword(password) != 1:
        password = input("Enter password: ")

    combiUserPass = user + " " + password + "\n"
    fileWrite.write(combiUserPass)
    fileWrite.close()
            
login()