#Checks if there are more than 5 or more accounts in the txt file
def accountLimit():
    userCount = 0
    fileOpen = open("users.txt", "r")
    for elements in open("users.txt", "r"):
        userCount+=1
    return userCount