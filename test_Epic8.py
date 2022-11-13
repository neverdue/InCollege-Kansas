import pytest
import json
import datetime
from Code.Source.globalVariables import dataFileInit, userInit, stackInit, getUser
from Code.Source.homePageOptions import deleteJobPost, updateLastLogin
from Code.Source.loginPrompt import register
from Code.Source.menu import homePage
from Code.Source.utility import writeJson, wJson

TESTMODE = True
ACCOUNT_FILE = 'Code/Data/accounts-test.json'
APPLICATION_FILE = 'Code/Data/applications-test.json'
JOB_FILE = 'Code/Data/jobPosts-test.json'
NOINPUT = OSError
MOCKTIME = datetime.datetime(2022, 11, 11, 0, 0, 0) 

@pytest.fixture(autouse=True)
def setup(): 
    dataFileInit(TESTMODE)
    stackInit()
    getAccountInfo()
    initUser(True)

def getAccountInfo():
    with open(ACCOUNT_FILE) as acc_file:
        data = json.load(acc_file)
        for account in data["accounts"]:
            if account["username"] == "testuser2":
               pytest.account = account
               break

def initUser(useMockTime=False):
    if useMockTime:
        userInit(pytest.account["username"], pytest.account["firstName"], pytest.account["lastName"], pytest.account["language"], pytest.account["email"], pytest.account["SMS"], pytest.account["ads"], pytest.account["subscription"], pytest.account["incomingRequests"], pytest.account["outgoingRequests"], pytest.account["friendsList"], pytest.account["profile"], pytest.account["registrationTime"], MOCKTIME.strftime("%m/%d/%Y %H:%M:%S"))
    else: 
        userInit(pytest.account["username"], pytest.account["firstName"], pytest.account["lastName"], pytest.account["language"], pytest.account["email"], pytest.account["SMS"], pytest.account["ads"], pytest.account["subscription"], pytest.account["incomingRequests"], pytest.account["outgoingRequests"], pytest.account["friendsList"], pytest.account["profile"], pytest.account["registrationTime"], pytest.account["lastLogin"])

# Mock time for functions that call datetime.datetime.now() (set to 11/11/2022 00:00:00)
@pytest.fixture
def patch_datetime_now(monkeypatch):
    class mydatetime(datetime.datetime):
        @classmethod
        def now(cls):
            return MOCKTIME
    monkeypatch.setattr(datetime, 'datetime', mydatetime)

@pytest.mark.parametrize("test_application_dict, isPassed", 
[(None, False), # Didn't apply
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
    job_data = json.load(open(JOB_FILE))
    deleteJobPost(jobID) # Temporarily delete job post for unit testing
    try:
        homePage()
    except NOINPUT:
        out, err = capsys.readouterr()
        assert f"*A job that you applied for has been deleted, Job Title: {jobTitle}" in out 
    writeJson(job_data, JOB_FILE)

# TEST: notify old students about new student(s) joining InCollege
@pytest.mark.parametrize("new_students", [
    [["test1", "Password123!", "Jongseong", "Park", True]],
    [["test1", "Password123!", "Jongseong", "Park", True], ["test2", "Password123!", "Yoongi", "Min", True]]
])
def test_newStudentsNotification(capsys, new_students): 
    message = ""
    data = json.load(open(ACCOUNT_FILE))
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
    wJson(data, ACCOUNT_FILE)
