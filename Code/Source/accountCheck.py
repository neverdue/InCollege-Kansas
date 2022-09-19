#Checks if the username is already taken
def accountExist(username, TESTMODE = False):
    if TESTMODE == True:
        fileOpen = open("users-test.txt", "r")
    else:
        fileOpen = open("users.txt", "r")
    for elements in fileOpen:
        users = elements.split()
        if(username == users[0]):
            return 1
    fileOpen.close()
    return 0