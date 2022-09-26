
# PAGE KEY:
# Login page = "main"
# Home page = "home"
# Find a job = "job"
# Find someone = "findSomeone"
# Learn new skill = "learnSkill"

#Initializes stack as global variable
def stackInit():
    global pageStack
    pageStack = []

#Append a page to stack (move pages)
def addPage(pageName):
    pageStack.append(pageName)

#Remove page from stack (go back a page)
def removePage():
    if(len(pageStack) > 1):
            #the first pop is to clear the current page from pageStack
            currentPage = pageStack.pop()
            #the second pop is to clear the page we are going to, because otherwise we could get a scenario of [p1, p2, p3] goes to next page and now [p1, p2, p3, p3]
            lastPage = pageStack.pop()
    else:
        return pageStack

    return lastPage

def printStack():
    print(pageStack)

#User variable stores username, firstname, lastname
def userInit(user, first, last):
    global loggedUser
    loggedUser = {
        "username" : user,
        "firstName" : first,
        "lastName" : last
    }

def getFirst():
    return loggedUser.get("firstName")

def getLast():
    return loggedUser.get("lastName")

def getUser():
    return loggedUser.get("username")