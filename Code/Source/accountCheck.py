#Checks if the username is already taken
def accountExist(username):
    fileOpen = open("users.txt", "r")
    for elements in fileOpen:
        users = elements.split()
        if(username == users[0]):
            return 1
    fileOpen.close()
    return 0