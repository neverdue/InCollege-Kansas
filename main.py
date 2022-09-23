from Code.Source.loginPrompt import register, login
from Code.Source.accountCount import accountLimit
from Code.Source.home_page import homePage, readJobPosts
from Code.Source.globalVariables import init, addPage, removePage, pageStack

def main():
    #Read in jobPosts at start up
    jobPosts = readJobPosts()

    #Initialize stack and add login page
    init()
    addPage("main")

    fileWrite = open("users.txt", "a")
    try:
        menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))
    except:
        print("Invalid input!")
        return
    loggedIn = False

    while (menuSelection != 1 and menuSelection != 2):
        print("Invalid selection, please try again.\n")
        try:
            menuSelection = int(input("Select 1 to login to an existing account\nSelect 2 to register a new account\nSelection: "))
        except:
            print("Invalid input!")
            return

    if menuSelection == 1 and accountLimit() != 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if login(username, password) == 1:
            loggedIn = True
    elif menuSelection == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        register(username, password)
    
    if loggedIn == True:
        homePage()
    
    fileWrite.close()

if __name__ == "__main__":
    main()