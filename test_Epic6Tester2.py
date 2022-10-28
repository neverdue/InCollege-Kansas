from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUserProfile, stackInit, userInit
from Code.Source.homePageOptions import createProfile, displayProfile, showAllJobs, showHomePageGreeting, showProfile, showMyNetwork
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage
from Code.Source.loginPrompt import register
from Code.Source.utility import addToFriendsList, createRequest, terminateProgram,  writeJson
import io
import pytest
import json

TESTMODE = True
JOBFILE = 'Code/Data/jobPosts-test.json'
DATAFILE = 'Code/Data/accounts-test.json'
APPLICATIONSFILE = 'Code/Data/applications-test.json'

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    addPage(homePage)
    open(APPLICATIONSFILE, 'w').close()
    open(JOBFILE, 'w').close()
    jobs = {
        "numPosts": 5,
        "currentIDs": 5,
        "jobPosts": [
            {
                "id": "1",
                "Title": "Job1",
                "Description": "Work",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "John Smith"
            },
            {
                "id": "2",
                "Title": "Job2",
                "Description": "Work to live",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "John Smith"
            },
            {
                "id": "3",
                "Title": "Job3",
                "Description": "Working is good",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Andy Nguyen"
            },
            {
                "id": "4",
                "Title": "Job4",
                "Description": "Work is worship",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "John Smith"
            },
            {
                "id": "5",
                "Title": "Job5",
                "Description": "Work is okay",
                "Employer": "Apple",
                "Location": "Silicon Valley",
                "Salary": "$300,000",
                "Name": "Andy Nguyen"
            }
        ]
    }
    applications = {
        "testuser": {
            "90": {
                "graduationDate": "02/25/1997",
                "startDate": "02/25/1998",
                "paragraph": "gimme you money"
            }
        },
        "user1": {
            "4": {
                "graduationDate": "02/25/1997",
                "startDate": "02/25/1997",
                "paragraph": "MONEY"
            },
            "2": {
                "graduationDate": "02/25/1997",
                "startDate": "02/25/1997",
                "paragraph": "fun"
            },
            "1": {
                "graduationDate": "02/25/1997",
                "startDate": "02/25/1997",
                "paragraph": "money"
            }
        }
    }
    writeJson(applications, APPLICATIONSFILE)
    writeJson(jobs, JOBFILE)

    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        test_data = data["accounts"][0]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
        pytest.profile = {"experience": [], "education": []}
    userInit(pytest.username, pytest.first, pytest.last, "English", True, True, True, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile)

def test_seeAllJobs(capfd, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    showAllJobs()
    out, err = capfd.readouterr()
    jobTitle = "Job{}"
    for i in range(1, 6):
        assert jobTitle.format(i) in out

@pytest.mark.parametrize("testInputs, messages", 
[
    (['1'], ["Title : Job1", "Description : Work", "Employer : Apple", "Location : Silicon Valley", "Salary : $300,000", "Name : John Smith"]),
    (['2'], ["Title : Job2", "Description : Work", "Employer : Apple", "Location : Silicon Valley", "Salary : $300,000", "Name : John Smith"]),
    (['3'], ["Title : Job3", "Description : Work", "Employer : Apple", "Location : Silicon Valley", "Salary : $300,000", "Name : Andy Nguyen"]),
    (['4'], ["Title : Job4", "Description : Work", "Employer : Apple", "Location : Silicon Valley", "Salary : $300,000", "Name : John Smith"]),
    (['5'], ["Title : Job5", "Description : Work", "Employer : Apple", "Location : Silicon Valley", "Salary : $300,000", "Name : Andy Nguyen"])
])
def test_seeJobInfo(capfd, monkeypatch, testInputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: testInputs.pop(0))
        showAllJobs()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

@pytest.mark.parametrize("testInputs, messages", 
[
    (['3', '1'], ["Title : Job3", "You can't apply to a job you've posted"]),
    (['5', '1'], ["Title : Job5", "You can't apply to a job you've posted"])
])
def test_restrictApplyToOwnJob(capfd, monkeypatch, testInputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: testInputs.pop(0))
        showAllJobs()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

@pytest.mark.parametrize("testInputs, messages", 
[
    (['1', '1'], ["Title : Job1", "You cannot apply to a job you've already applied to"]),
    (['2', '1'], ["Title : Job2", "You cannot apply to a job you've already applied to"]),
    (['4', '1'], ["Title : Job4", "You cannot apply to a job you've already applied to"])
])
def test_restrictReApply(capfd, monkeypatch, testInputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: testInputs.pop(0))
        showAllJobs()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out
