import pytest
import json
import datetime
from io import StringIO
from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUser, getUserProfile, stackInit, userInit, logout
from Code.Source.loginPrompt import signUpPage
from Code.Source.utility import writeJson, wJson
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage, jobPage, newJobNotification


TESTMODE = True
DATAFILE = 'Code/Data/accounts-test.json'
MESSAGEFILE = 'Code/Data/inbox-test.json'
JOBFILE = 'Code/Data/jobPosts-test.json'

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    email = True
    sms = True
    ads = True
    subscription = False

    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        #using index1
        indexForUser1 = 0
        test_data = data["accounts"][indexForUser1]
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
                "education": []
            },
            "registrationTime": "11/01/2022 23:59:59",
            "lastLogin": "11/09/2022 13:59:15"
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
                "education": []
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
            },
            {
            "username": "user7",
            "password": "Password123!",
            "firstName": "Mayank",
            "lastName": "Pandey",
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
            "registrationTime": "11/09/2022 13:58:30",
            "lastLogin": "11/09/2022 14:01:16"
            }
        ]
        }
    writeJson(accounts, DATAFILE)

    creationTime = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    open(JOBFILE)
    jobs = {
        "numPosts": 8,
        "currentIDs": 5,
        "jobPosts": [
            {
                "id": "1",
                "Title": "Job1",
                "Description": "Work",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "John Smith",
                "TimeCreated": "11/01/2022 23:59:59"
            },
            {
                "id": "2",
                "Title": "Job2",
                "Description": "Work to live",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "John Smith",
                "TimeCreated": "11/01/2022 23:59:59"
            },
            {
                "id": "3",
                "Title": "Job3",
                "Description": "Working is good",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Spoopy Ando",
                "TimeCreated": "11/01/2022 23:59:59"
            },
            {
                "id": "4",
                "Title": "Job4",
                "Description": "Work is worship",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "John Smith",
                "TimeCreated": creationTime
            },
            {
                "id": "5",
                "Title": "Job5",
                "Description": "Work is okay",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Andy Nguyen",
                "TimeCreated": "11/01/2022 23:59:59"
            },
            {
                "id": "6",
                "Title": "Job6",
                "Description": "Deletion pytest",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Andy Nguyen",
                "TimeCreated": "11/01/2022 23:59:59"
            },
            {
                "id": "7",
                "Title": "Job7",
                "Description": "app pytest",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Andy Nguyen",
                "TimeCreated": "11/01/2022 23:59:59"
            },
            {
                "id": "8",
                "Title": "Job8",
                "Description": "save pytest",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Andy Nguyen",
                "TimeCreated": "11/01/2022 23:59:59"
            }
        ]
    }
    writeJson(jobs, JOBFILE)


#Rewrites job creation time in line 261 so you can test whenever and it wouldn't be using an old date
def test_newJobNotif(capfd):
    newJobNotification()
    
    out, err = capfd.readouterr()
    assert "A new job" in out

def test_jobApplyNotif(capfd):
    try:
        jobPage()
    except OSError:
        out, err = capfd.readouterr()
        assert "You have currently applied for" in out

def test_createProfileNotif(capfd):
    try:
        homePage()
    except OSError:
        out, err = capfd.readouterr()
        assert "Don't forget to create a profile!" in out

def test_newMessageNotif(capfd):
    try:
        homePage()
    except OSError:
        out, err = capfd.readouterr()
        assert "You have messages" in out
