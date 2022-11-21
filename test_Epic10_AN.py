import io
import pytest
import json
import datetime
from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUser, getUserProfile, setExperienceInfo, stackInit, userInit, logout, getJobFile
from Code.Source.homePageOptions import addJobPost, createProfile, deleteJobMenu
from Code.Source.inputAPI import inputAPIs
from Code.Source.loginPrompt import signUpPage
from Code.Source.menu import homePage
from Code.Source.menuOptions import back
from Code.Source.outputAPI import outputAPIs
from Code.Source.mainPage import mainPage
from Code.Source.utility import writeJson
from main import main


TESTMODE = True
JOBFILE = 'Code/Data/jobPosts-test.json'
NEW_JOB_APIFILE = 'Code/ApiData/newJobs-test.txt'
STUDENT_ACCOUNTS = 'Code/ApiData/studentAccounts-test.txt'
MYCOLLEGE_APPLIEDJOBS= 'Code/ApiData/MyCollege_appliedJobs.txt'
MYCOLLEGE_JOBS = 'Code/ApiData/MyCollege_jobs.txt'
MYCOLLEGE_PROFILES = 'Code/ApiData/MyCollege_profiles.txt'
MYCOLLEGE_SAVEDJOBS = 'Code/ApiData/MyCollege_savedJobs.txt'
MYCOLLEGE_USER = 'Code/ApiData/MyCollege_user.txt'

DATAFILE = 'Code/Data/accounts-test.json'
APPLICATIONFILE = 'Code/Data/applications-test.json'

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()

    email = True
    sms = True
    ads = True
    subscription = False

    creationTime = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        #using index1
        indexForUser3 = 2
        test_data = data["accounts"][indexForUser3]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
        pytest.profile = {"experience": [], "education": []}
    userInit(pytest.username, pytest.first, pytest.last, "English", email, sms, ads, subscription, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile, "11/01/2022 23:59:59", "11/01/2022 23:59:59")
    open(DATAFILE)
    accounts = {
        "accounts": [
            {
            "username": "user1",
            "password": "Password123!",
            "firstName": "Andy",
            "lastName": "Nguyen",
            "language": "Spanish",
            "email": "False",
            "SMS": "False",
            "ads": "True",
            "subscription": "False",
            "incomingRequests": [
                "user2"
            ],
            "outgoingRequests": [],
            "friendsList": [
                "user2"
            ],
            "profile": {
                "experience": [],
                "education": [
                    {
                        "school name": "usf",
                        "degree": "cs",
                        "years attended": "4"
                    }
                ],
                "title": "PROFILE TITLE EXAMPLE",
                "major": "PROFILE MAJOR EXAMPLE",
                "university": "PROFILE UNIVERSITY EXAMPLE",
                "about": "PARAGRAPH ABOUT EXAMPLE"
            },
            "registrationTime": "11/01/2022 23:59:59",
            "lastLogin": creationTime
            },
            {
            "username": "user2",
            "password": "Password123*",
            "firstName": "Spoopy",
            "lastName": "Ando",
            "language": "English",
            "email": "True",
            "SMS": "True",
            "ads": "True",
            "subscription": "False",
            "incomingRequests": [
                "testuser1"
            ],
            "outgoingRequests": [
                "testuser2"
            ],
            "friendsList": [
                "user1",
                "testuser3"
            ],
            "profile": {
                "experience": [],
                "education": [
                {
                    "school name": "usf",
                    "degree": "cs",
                    "years attended": "4"
                }
                ],
                "title": "Title Example",
                "major": "Computer Science",
                "university": "Universitytest",
                "about": "Paragraph about myself!!!"
            },
            "registrationTime": "11/02/2022 23:59:59",
            "lastLogin": "11/02/2022 23:59:59"
            },
            {
            "username": "testuser1",
            "password": "Password123@",
            "firstName": "tommy",
            "lastName": "truong",
            "language": "English",
            "email": "True",
            "SMS": "True",
            "ads": "True",
            "subscription": "True",
            "incomingRequests": [],
            "outgoingRequests": [
                "user2"
            ],
            "friendsList": [
                "testuser2"
            ],
            "profile": {
                "experience": [],
                "education": [],
            },
            "registrationTime": "11/03/2022 23:59:59",
            "lastLogin": "11/03/2022 23:59:59"
            },
            {
            "username": "testuser2",
            "password": "Password123$",
            "firstName": "kevin",
            "lastName": "vu",
            "language": "English",
            "email": "True",
            "SMS": "True",
            "ads": "True",
            "subscription": "False",
            "incomingRequests": [
                "user2"
            ],
            "outgoingRequests": [],
            "friendsList": [
                "testuser1"
            ],
            "profile": {
                "experience": [],
                "education": []
            },
            "registrationTime": "11/04/2022 23:59:59",
            "lastLogin": "11/04/2022 23:59:59"
            },
            {
            "username": "testuser3",
            "password": "Password123@",
            "firstName": "Testyy",
            "lastName": "Pythony",
            "language": "English",
            "email": "True",
            "SMS": "True",
            "ads": "True",
            "subscription": "False",
            "incomingRequests": [],
            "outgoingRequests": [],
            "friendsList": [
                "user2"
            ],
            "profile": {
                "experience": [],
                "education": []
            },
            "registrationTime": "11/05/2022 23:59:59",
            "lastLogin": "11/05/2022 23:59:59"
            },
            {
            "username": "subTest",
            "password": "Password123!",
            "firstName": "ash",
            "lastName": "mer",
            "language": "English",
            "email": "True",
            "SMS": "True",
            "ads": "True",
            "subscription": "True",
            "incomingRequests": [],
            "outgoingRequests": [],
            "friendsList": [],
            "profile": {
                "experience": [],
                "education": []
            },
            "registrationTime": "11/06/2022 23:59:59",
            "lastLogin": "11/06/2022 23:59:59"
            }
        ]
    }
    writeJson(accounts, DATAFILE)

    open(APPLICATIONFILE)
    fileContents = {
        "deletedApplications": {
            "user2": [
                "Job6"
            ]
        },
        "applications": {
            "testuser": {
                "90": {
                    "Title": "Job90",
                    "graduationDate": "02/25/1997",
                    "startDate": "02/25/1998",
                    "paragraph": "gimme you money",
                    "WhenApplied": "11/01/2022 10:50:30"
                }
            },
            "user1": {
                "1": {
                    "Title": "Job1",
                    "graduationDate": "01/01/2025",
                    "startDate": "01/01/2025",
                    "paragraph": "A",
                    "WhenApplied": "01/01/2022 00:00:00"
                },
                "2": {
                    "Title": "Job2",
                    "graduationDate": "01/01/2025",
                    "startDate": "01/01/2025",
                    "paragraph": "A",
                    "WhenApplied": "11/10/2022 00:00:00"
                }
            },
            "user2": {
                "8": {
                    "Title": "Job8",
                    "graduationDate": "01/23/2022",
                    "startDate": "01/06/2018",
                    "paragraph": "money",
                    "WhenApplied": "11/01/2022 10:50:30"
                }
            }
        },
        "saved": {
            "user2": [
                "1"
            ],
            "user1": [
                "1"
            ]
        }
    }
    writeJson(fileContents, APPLICATIONFILE)

def test_outputAppliedJobs():
    # Adding to newJobs-test.txt file
    stringInput = "TestTitle\nTestDescription\n&&&\nTestFName TestLName\nTestLocation\nTestLocation2\n$00000\n=====\n"
    tokenizedInput = ["TestTitle\n", "TestDescription\n", "&&&\n", "TestFName TestLName\n", "TestLocation\n", "TestLocation2\n", "$00000\n", "=====\n"]
    lengthList = len(tokenizedInput)
    matchCount = 0

    # Preventing duplicates from being written in the test file 
    with open(NEW_JOB_APIFILE, "r") as file:
        for items in tokenizedInput:
            if items in file:
                matchCount+=1

    if matchCount != lengthList:
        with open(NEW_JOB_APIFILE, "a") as txtFile:
            txtFile.write(stringInput)
        txtFile.close()
    file.close()

    inputAPIs()
    outputAPIs()
    
    # Assertion
    with open(MYCOLLEGE_APPLIEDJOBS, "r") as txtFile:
        assert "TestTitle\n" in txtFile  
    txtFile.close()

def test_outputJobs():
    # Adding to newJobs-test.txt file
    stringInput = "TestTitle\nTestDescription\n&&&\nTestFName TestLName\nTestLocation\nTestLocation2\n$00000\n=====\n"
    tokenizedInput = ["TestTitle\n", "TestDescription\n", "&&&\n", "TestFName TestLName\n", "TestLocation\n", "TestLocation2\n", "$00000\n", "=====\n"]
    lengthList = len(tokenizedInput)
    matchCount = 0

    # Preventing duplicates from being written in the test file 
    with open(NEW_JOB_APIFILE, "r") as file:
        for items in tokenizedInput:
            if items in file:
                matchCount+=1

    if matchCount != lengthList:
        with open(NEW_JOB_APIFILE, "a") as txtFile:
            txtFile.write(stringInput)
        txtFile.close()
    file.close()

    inputAPIs()
    outputAPIs()

    # Assertion
    stringList = ['TestTitle\n', 'TestDescription\n', '&&&\n', 'TestLocation\n', 'TestLocation2\n', '$00000\n', '=====\n']
    with open(MYCOLLEGE_JOBS, "r") as txtFile:
        for items in stringList:
            assert items in txtFile
    txtFile.close()

# Hard codes data and overwrites accounts-test.json on lines 49-88. Uses those hard coded values for assertions
def test_outputProfiles():
    assertionList = ['PROFILE TITLE EXAMPLE\n', 'PROFILE MAJOR EXAMPLE\n', 'PROFILE UNIVERSITY EXAMPLE\n', 'PARAGRAPH ABOUT EXAMPLE\n', 'usf cs 4 \n', '=====\n']
    with open(MYCOLLEGE_PROFILES, "r") as txtFile:
        for items in assertionList:
            assert items in txtFile
    txtFile.close()


# Hard codes data and overwrites applications-test.json on lines 90-142. Uses those hard coded values for assertions
def test_outputSavedJobs():
    assertionList = ['user1,Job1\n', '=====\n']
    with open(MYCOLLEGE_SAVEDJOBS, "r") as txtFile:
        for items in assertionList:
            assert items in txtFile
    txtFile.close()

def test_outputUsers():
    assertionList = ['user1 standard\n', '=====\n']
    with open(MYCOLLEGE_USER, "r") as txtFile:
        for items in assertionList:
            assert items in txtFile
    txtFile.close()

# Checking to see if the files have been created
def test_profilesCheck():
    assert open(MYCOLLEGE_PROFILES)

def test_savedJobsCheck():
    assert open(MYCOLLEGE_SAVEDJOBS)

def test_JobsCheck():
    assert open(MYCOLLEGE_JOBS)

def test_appliedJobsCheck():
    assert open(MYCOLLEGE_APPLIEDJOBS)

def test_usersCheck():
    assert open(MYCOLLEGE_USER)

#When a user creates a profile, the profile should be added to MyCollege_profiles.txt
@pytest.mark.parametrize("inputs", 
[
    (
        ["TESTTITLE", "y", "TESTMAJOR", "y", "TESTUNI", "y", "TESTPARA", "y", "y", "TEST", "TEST", "11/11/1111", "11/11/1111", "TEST", "TEST", "n", "y", "TEST", "TEST", "4"]
    )
]
)
def test_createProfile(monkeypatch, inputs):
    try:
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(inputs)))
        createProfile()
        inputAPIs()
        outputAPIs()
    except EOFError:
        #"Testmajor\n", "Testuni\n", "TESTPARA\n", "TEST TEST 11/11/1111 11/11/1111 TEST TEST\n", "TEST TEST 4\n", "=====\n"
        assertList = ["TESTTITLE\n", "Testmajor\n", "Testuni\n", "TESTPARA\n", "TEST TEST 11/11/1111 11/11/1111 TEST TEST \n", "TEST TEST 4 \n", "=====\n"]
        with open(MYCOLLEGE_PROFILES, "r") as txtFile:
            for tokens in assertList:
                assert tokens in txtFile
        txtFile.close()

# When a job is created, add to MyCollege_jobs.txt
@pytest.mark.parametrize("inputs", 
[
    (
        ["TESTJOB", "TESTDESCRIPTION", "TESTEMPLOYER", "TESTLOCATION", "$00000", "n"]
    )
]
)
def test_createJob(monkeypatch, inputs):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(inputs)))
    addJobPost()
    inputAPIs()
    outputAPIs()

    assertList = ["TESTJOB\n", "TESTDESCRIPTION\n", "&&&\n", "TESTEMPLOYER\n", "TESTLOCATION\n", "$00000\n", "=====\n"]
    with open(MYCOLLEGE_JOBS) as txtFile:
        for tokens in assertList:
            assert tokens in txtFile

    txtFile.close()

# When a new user creates an account, add the user account to MyCollege_users.txt
@pytest.mark.parametrize("inputs", 
[
    (
        ["burrito", "Password123!", "burrito", "tran", "no"]
    )
]
)
def test_createAccount(monkeypatch, inputs):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(inputs)))
    logout()
    signUpPage()
    inputAPIs()
    outputAPIs()

    assertList = ["burrito standard\n", "=====\n"]
    with open(MYCOLLEGE_USER) as txtFile:
        for tokens in assertList:
            assert tokens in txtFile
    txtFile.close()

# When a job is deleted, recreate MyCollege_jobs.txt with deleted job removed
@pytest.mark.parametrize("inputs", 
[
    (
        ["1"]
    )
]
)
def test_deleteJob(monkeypatch, inputs):
    #try:
        stackInit()
        addPage()
        monkeypatch.setattr('sys.stdin', io.StringIO((inputs)))
        jobDict = {
                "id": "8",
                "Title": "Job8",
                "Description": "save pytest",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "tommy truong",
                "TimeCreated": "11/01/2022 23:59:59"
            }
        deleteJobMenu(jobDict)
        #inputAPIs()
        outputAPIs()

    #except EOFError:
        assertList = ["Job8"]
        with open(MYCOLLEGE_USER) as txtFile:
            for tokens in assertList:
                assert tokens not in txtFile
        txtFile.close()



