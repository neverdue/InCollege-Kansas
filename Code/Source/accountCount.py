#Checks if there are more than 5 or more accounts in the txt file
def accountLimit(TESTMODE = False):
    userCount = 0
    if TESTMODE == True:
        fileOpen = open("users-test.txt", "r")
    else:
        fileOpen = open("users.txt", "r")
    for elements in fileOpen:
        userCount+=1
    return userCount