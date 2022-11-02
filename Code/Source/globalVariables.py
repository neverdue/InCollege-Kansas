# Global variables
PROFILE_KEYS = ["title", "major", "university", "about", "experience", "education"]
EXPERIENCE_KEYS = ["title", "employer", "date started", "date ended", "location", "description"]
EDUCATION_KEYS = ["school name", "degree", "years attended"]

# Initialize the data file and job file as global variables so that they can be accessed from any file
def dataFileInit(TESTMODE = False):
    global dataFile
    global jobFile
    global applicationsFile
    global timer
    if TESTMODE == False:
        dataFile = "Code/Data/accounts.json"
        jobFile = "Code/Data/jobPosts.json"
        applicationsFile = "Code/Data/applications.json"
        timer = 0
    else:
        dataFile = "Code/Data/accounts-test.json"
        jobFile = "Code/Data/jobPosts-test.json"
        applicationsFile = "Code/Data/applications-test.json"
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
def userInit(user, first, last, language, email, sms, ads, subscription, incomingRequests = [], outgoingRequests = [], friendsList = [], profile = {}):
    global loggedUser
    loggedUser = {
        "username" : user,
        "firstName" : first,
        "lastName" : last,
        "language" : language,
        "emailPref" : email,
        "SMSPref" : sms,
        "adPref" : ads,
        "subscription": subscription,
        "incomingRequests" : incomingRequests,
        "outgoingRequests" : outgoingRequests,
        "friendsList" : friendsList,
        "profile": profile
    }

def logout():
    global loggedUser
    loggedUser = None

def getLoggedUser():
    return loggedUser

def getFirst():
    return loggedUser.get("firstName").title()

def getLast():
    return loggedUser.get("lastName").title()

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

def getIfSubcribed():
    return loggedUser.get("subscription")

def setifSubscribed(x):
    loggedUser["subscription"] = x

def getIncomingRequests():
    return loggedUser.get("incomingRequests")

def setIncomingRequests(x):
    loggedUser["incomingRequests"] = x

def getOutgoingRequests():
    return loggedUser.get("outgoingRequests")

def setOutgoingRequests(x):
    loggedUser["outgoingRequests"] = x

def getFriendsList():
    return loggedUser.get("friendsList")

def setFriendsList(x):
    loggedUser["friendsList"] = x



def getUserProfile():
    return loggedUser["profile"]

def setProfileInfo(key, info):
    loggedUser["profile"][key] = info

def setExperienceInfo(info):
    loggedUser["profile"]["experience"].append(info)

def setEducationInfo(info):
    loggedUser["profile"]["education"].append(info)
    
def getExperienceCount():
    return len(loggedUser["profile"]["experience"])
    
def getEducationCount():
    return len(loggedUser["profile"]["education"])

def getApplicationsFile():
    return applicationsFile