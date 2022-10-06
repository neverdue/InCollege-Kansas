# Initialize the data file and job file as global variables so that they can be accessed from any file
def dataFileInit(TESTMODE = False):
    global dataFile
    global jobFile
    global settingFile
    if TESTMODE == False:
        dataFile = "Code/Data/accounts.json"
        jobFile = "Code/Data/jobPosts.json"
        settingFile = "Code/Data/userSettings.json"
    else:
        dataFile = "Code/Data/accounts-test.json"
        jobFile = "Code/Data/jobPosts-test.json"
        settingFile = "Code/Data/userSettings-test.json"

def getDataFile():
    return dataFile

def getJobFile():
    return jobFile

def getSettingFile():
    return settingFile

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
def userInit(user, first, last, language, email, sms, ads):
    global loggedUser
    loggedUser = {
        "username" : user,
        "firstName" : first,
        "lastName" : last,
        "language" : language,
        "emailPref" : email,
        "SMSPref" : sms,
        "adPref" : ads
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

def getEmailPref():
    return loggedUser.get("emailPref")

def getSMSPref():
    return loggedUser.get("SMSPref")

def getAdPref():
    return loggedUser.get("adPref")