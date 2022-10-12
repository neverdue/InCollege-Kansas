# Initialize the data file and job file as global variables so that they can be accessed from any file
def dataFileInit(TESTMODE = False):
    global dataFile
    global jobFile
    global timer
    if TESTMODE == False:
        dataFile = "Code/Data/accounts.json"
        jobFile = "Code/Data/jobPosts.json"
        timer = 0
    else:
        dataFile = "Code/Data/accounts-test.json"
        jobFile = "Code/Data/jobPosts-test.json"
        timer = 0

def getDataFile():
    return dataFile

def getJobFile():
    return jobFile

def getTimer():
    return timer


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
def userInit(user, first, last, university, major, language, email, sms, ads, incomingRequests = [], outgoingRequests = [], friends = []):
    global loggedUser
    loggedUser = {
        "username" : user,
        "firstName" : first,
        "lastName" : last,
        "university" : university,
        "major" : major,
        "language" : language,
        "emailPref" : email,
        "SMSPref" : sms,
        "adPref" : ads,
        "incomingRequests" : incomingRequests,
        "outgoingRequests" : outgoingRequests,
        "friends" : friends
    }

def logout():
    global loggedUser
    loggedUser = None

def getLoggedUser():
    return loggedUser

def getFirst():
    return loggedUser.get("firstName")

def getLast():
    return loggedUser.get("lastName")

def getUser():
    return loggedUser.get("username")

def getLang():
    return loggedUser.get("language")

def setLang(x):
    loggedUser["language"] = x

def getEmailPref():
    return loggedUser.get("emailPref")

def setEmailPref(x):
    loggedUser["email"] = x

def getSMSPref():
    return loggedUser.get("SMSPref")

def setSMSPref(x):
    loggedUser["SMS"] = x

def getAdPref():
    return loggedUser.get("adPref")

def setAdPref(x):
    loggedUser["ads"] = x

def getIncomingRequests():
    return loggedUser.get("incomingRequests")

def setIncomingRequests(x):
    loggedUser["incomingRequests"] = x

def getOutgoingRequests():
    return loggedUser.get("outgoingRequests")

def setOutgoingRequests(x):
    loggedUser["outgoingRequests"] = x

def getFriends():
    return loggedUser.get("friends")

def setFriends(x):
    loggedUser["friends"] = x