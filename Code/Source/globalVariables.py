# Global variables
PROFILE_KEYS = ["title", "major", "university", "about", "experience", "education"]
EXPERIENCE_KEYS = ["title", "employer", "date started", "date ended", "location", "description"]
EDUCATION_KEYS = ["school name", "degree", "years attended"]

# Initialize the data file and job file as global variables so that they can be accessed from any file
def dataFileInit(TESTMODE = False):
    global dataFile
    global jobFile
    global applicationsFile
    global messageFile
    global accountsFile
    global MyCollege_jobs
    global MyCollege_appliedJobs
    global MyCollege_savedJobs
    global newJobs
    global timer
    global studentAccounts
    global MyCollege_user
    global MyCollege_profiles
    newJobs = 'Code/ApiData/newJobs.txt'
    MyCollege_jobs = 'Code/ApiData/MyCollege_jobs.txt'
    MyCollege_appliedJobs = 'Code/ApiData/MyCollege_appliedJobs.txt'
    MyCollege_savedJobs = 'Code/ApiData/MyCollege_savedJobs.txt'
    studentAccounts = 'Code/ApiData/studentAccounts.txt'
    MyCollege_user =  'Code/ApiData/MyCollege_user.txt'
    MyCollege_profiles =  'Code/ApiData/MyCollege_profiles.txt'
    if TESTMODE == False:
        dataFile = "Code/Data/accounts.json"
        jobFile = "Code/Data/jobPosts.json"
        applicationsFile = "Code/Data/applications.json"
        messageFile = "Code/Data/inbox.json"
        accountsFile = "Code/Data/accounts-test.json"
        timer = 0
    else:
        dataFile = "Code/Data/accounts-test.json"
        jobFile = "Code/Data/jobPosts-test.json"
        applicationsFile = "Code/Data/applications-test.json"
        messageFile = "Code/Data/inbox-test.json"
        accountsFile = "Code/Data/accounts.json"
        timer = 0

def getDataFile():
    return dataFile

def getJobFile():
    return jobFile

def getApplicationsFile():
    return applicationsFile

def getMessageFile():
    return messageFile

def getAccountsFile():
    return accountsFile

def getMyCollege_jobs():
    return MyCollege_jobs

def getMyCollege_appliedJobs():
    return MyCollege_appliedJobs

def getMyCollege_savedJobs():
    return MyCollege_savedJobs

def getNewJobs():
    return newJobs

def getTimer():
    return timer

def getStudentAccounts():
    return studentAccounts

def getMyCollege_profiles():
    return MyCollege_profiles

def getMyCollege_user():
    return MyCollege_user

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
def userInit(user, first, last, language, email, sms, ads, subscription, incomingRequests = [], outgoingRequests = [], friendsList = [], profile = {}, registrationTime = "", lastLogin = ""):
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
        "profile": profile,
        "registrationTime": registrationTime,
        "lastLogin": lastLogin
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

def getRegistrationTime():
    return loggedUser.get("registrationTime")

def getLastLogin():
    return loggedUser.get("lastLogin")

