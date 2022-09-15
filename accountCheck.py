#Checks if the username is already taken
def accountExist(username):
    x = range(0)
    fileOpen = open("users.txt", "r")
    for elements in fileOpen:
        users = elements.split()
        for names in range(len(users)):
            if(username == users[0]):
                print("Username '", username, "' already exists.")
                return 1
    fileOpen.close()