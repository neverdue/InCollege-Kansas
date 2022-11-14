import pytest
import json
import datetime
from io import StringIO
from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUser, getUserProfile, stackInit, userInit, logout
from Code.Source.loginPrompt import signUpPage, register
from Code.Source.utility import writeJson, wJson
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage, jobPage, newJobNotification
from Code.Source.homePageOptions import deleteJobPost, messageNotification, updateLastLogin


TESTMODE = True
DATAFILE = 'Code/Data/accounts-test.json'
APPLICATION_FILE = 'Code/Data/applications-test.json'
MESSAGEFILE = 'Code/Data/inbox-test.json'
JOBFILE = 'Code/Data/jobPosts-test.json'
MOCKTIME = datetime.datetime(2022, 11, 11, 0, 0, 0) 
NOINPUT = OSError

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    getAccountInfo()
    initUser()
    email = True
    sms = True
    ads = True
    subscription = False

    creationTime = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

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
            "lastLogin": creationTime
            }
        ]
        }
    writeJson(accounts, DATAFILE)

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

    open(MESSAGEFILE)
    mess = {
        "outgoing": {
            "user1": {
                "user2": [
                    "this is a message from user 1 to user2",
                    "pytest user2 and user1"
                ]
            },
            "testuser1": {
                "testuser2": [
                    "testing message from testuser1 to testuser2"
                ],
                "user2": [
                    "this is a message from testuser1, a subscribed person to user2",
                    "Pytest: I am a recruiter(plus member) messaging a standard user named user2"
                ]
            }
        },
        "incoming": {
            "user2": {
                "user1": [
                    "this is a message from user 1 to user2",
                    "pytest user2 and user1"
                ],
                "testuser1": [
                    "this is a message from testuser1, a subscribed person to user2",
                    "Pytest: I am a recruiter(plus member) messaging a standard user named user2"
                ]
            },
            "testuser2": {
                "testuser1": [
                    "testing message from testuser1 to testuser2"
                ]
            },
            "user1": {
                "user2": []
            }
        }
    }
    writeJson(mess, MESSAGEFILE)

def getAccountInfo():
    with open(DATAFILE) as acc_file:
        data = json.load(acc_file)
        for account in data["accounts"]:
            if account["username"] == "user1":
               pytest.account = account
               break

def initUser(useMockTime=False):
    if useMockTime:
        userInit(pytest.account["username"], pytest.account["firstName"], pytest.account["lastName"], pytest.account["language"], pytest.account["email"], pytest.account["SMS"], pytest.account["ads"], pytest.account["subscription"], pytest.account["incomingRequests"], pytest.account["outgoingRequests"], pytest.account["friendsList"], pytest.account["profile"], pytest.account["registrationTime"], MOCKTIME.strftime("%m/%d/%Y %H:%M:%S"))
    else: 
        userInit(pytest.account["username"], pytest.account["firstName"], pytest.account["lastName"], pytest.account["language"], pytest.account["email"], pytest.account["SMS"], pytest.account["ads"], pytest.account["subscription"], pytest.account["incomingRequests"], pytest.account["outgoingRequests"], pytest.account["friendsList"], pytest.account["profile"], pytest.account["registrationTime"], pytest.account["lastLogin"])

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

# Mock time for functions that call datetime.datetime.now() (set to 11/11/2022 00:00:00)
@pytest.fixture
def patch_datetime_now(monkeypatch):
    class mydatetime(datetime.datetime):
        @classmethod
        def now(cls):
            return MOCKTIME
    monkeypatch.setattr(datetime, 'datetime', mydatetime)

@pytest.mark.parametrize("test_application_dict, isPassed", 
[
# More than 7 days
({"1": {"Title": "Job1", "graduationDate": "01/01/2025", "startDate": "01/01/2025", "paragraph": "A", "WhenApplied": "11/03/2022 00:00:00"}},
True),
# Less than 7 days
({"1": {"Title": "Job1", "graduationDate": "01/01/2025", "startDate": "01/01/2025", "paragraph": "A", "WhenApplied": "11/10/2022 00:00:00"}}, 
False),
# Multiple applications: Most recent is more than 7 days 
({"1": {"Title": "Job1", "graduationDate": "01/01/2025", "startDate": "01/01/2025", "paragraph": "A", "WhenApplied": "11/03/2022 00:00:00"},
"2": {"Title": "Job2", "graduationDate": "01/01/2025", "startDate": "01/01/2025", "paragraph": "A", "WhenApplied": "01/01/2022 00:00:00"}},
True),
# Multiple applications: Most recent is less than 7 days
({"1": {"Title": "Job1", "graduationDate": "01/01/2025", "startDate": "01/01/2025", "paragraph": "A", "WhenApplied": "01/01/2022 00:00:00"},
"2": {"Title": "Job2", "graduationDate": "01/01/2025", "startDate": "01/01/2025", "paragraph": "A", "WhenApplied": "11/10/2022 00:00:00"}},
False)])

# TEST: notify students if they haven't applied for a job in the past 7 days 
def test_reminderToApplyNotification(capsys, patch_datetime_now, test_application_dict, isPassed):
    message = "Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!*"
    data = json.load(open(APPLICATION_FILE))
    if test_application_dict is not None:
        data["applications"][getUser()] = test_application_dict
    writeJson(data, APPLICATION_FILE)  
    try: 
        homePage()
    except NOINPUT: 
        out, err = capsys.readouterr()
        if isPassed:
            assert message in out # More than 7 days
        else: 
            assert message not in out # Less than 7 days 

# TEST: when a student logs in, notify if a job they have applied for was deleted (including job title)
@pytest.mark.parametrize("jobID, jobTitle", [("1", "Job1"), ("2", "Job2")])    
def test_deletedJobNotification(capsys, jobID, jobTitle): 
    job_data = json.load(open(JOBFILE))
    deleteJobPost(jobID) # Temporarily delete job post for unit testing
    try:
        homePage()
    except NOINPUT:
        out, err = capsys.readouterr()
        assert f"*A job that you applied for has been deleted, Job Title: {jobTitle}" in out 
    writeJson(job_data, JOBFILE)

# TEST: notify old students about new student(s) joining InCollege
@pytest.mark.parametrize("new_students", [
    [["test1", "Password123!", "Jongseong", "Park", True]],
    [["test1", "Password123!", "Jongseong", "Park", True], ["test2", "Password123!", "Yoongi", "Min", True]]
])
def test_newStudentsNotification(capsys, new_students): 
    message = ""
    data = json.load(open(DATAFILE))
    for student in new_students:
        register(student[0], student[1], student[2], student[3], student[4])
        message += f"\n\t*{student[2]} {student[3]} has joined InCollege*\n"
    initUser(True)
    try:
        homePage()
    except NOINPUT:
        out, err = capsys.readouterr()
        assert message in out

    # TEST: new students notifications should only appear once
    updateLastLogin()
    initUser()
    try:
        homePage()
    except NOINPUT:
        out, err = capsys.readouterr()
        assert message not in out # notification is not shown again
    wJson(data, DATAFILE)


#pytest test_Epic8_AN.py -rP