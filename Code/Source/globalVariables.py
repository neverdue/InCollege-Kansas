
# PAGE KEY:
# Login page = "main"
# Home page = "home"
# Find a job = "job"
# Find someone = "findSomeone"
# Learn new skill = "learnSkill"

#Initializes stack as global variable
def init():
    global pageStack
    pageStack = []

#Append a page to stack (move pages)
def addPage(pageName):
    pageStack.append(pageName)

#Remove page from stack (go back a page)
def removePage():
    currentPage = pageStack.pop()
    lastPage = pageStack.pop()
    return lastPage

def printStack():
    print(pageStack)