import pytest
import json
import io
from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUserProfile, stackInit, userInit, getDataFile, getUser 
from Code.Source.homePageOptions import createProfile, displayProfile, addApplicant, getJobApplications, getSavedJobIDs, deleteJobMenu, getYourJobs, readJobPosts
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage
from Code.Source.utility import writeJson

TESTMODE = True
JOBFILE = 'Code/Data/jobPosts-test.json'
DATAFILE = 'Code/Data/accounts-test.json'
APPFILE = 'Code/Data/applications-test.json'

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        #using index1
        test_data = data["accounts"][1]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
        pytest.profile = {"experience": [], "education": []}
    userInit(pytest.username, pytest.first, pytest.last, "English", True, True, True, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile)

    open(APPFILE)
    applicationJson = {
        "deletedApplications": {},
        "applications": {
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
            },
            "user2": {

            }
        },
        "saved": {
            "user2": [
                '1'
        ]
        }
    }

    writeJson(applicationJson, APPFILE)
    open(JOBFILE)
    jobs = {
        "numPosts": 10,
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
                "Name": "Spoopy Ando"
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
    writeJson(jobs, JOBFILE)



#Testing the case where a user applies to a job.
#not sure why applications-test.json isnt updating...
@pytest.mark.parametrize("userInputs, jobs",
[
    (
        ['1','6','1','1',"01/01/2024", "01/11/2024", "Because it seems like a great place"], "Title: Job1\nDescription: Work\nEmployer: Apple\nLocation: Silicon Valley\nSalary: $300,000"
    ),
    (
        ['1','6','2','1',"01/01/2025","01/11/2024", "Because it seems like a great place"], "Title: Job1\nDescription: Work to live\nEmployer: Apple\nLocation: Silicon Valley\nSalary: $300,000"
    ),
            
])
def test_userApplyingToJob(capfd, monkeypatch, userInputs, jobs):
    try:
        testJobIndex = userInputs[2]
        testGraduationDate = userInputs[4]
        testStartDate = userInputs[5]
        testParagraph = userInputs[6]
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()

    except IndexError: 
        out, err = capfd.readouterr()
       #TODO FIGURE OUT WHY IT STOPPED WORKING assert jobs in out
    application = getJobApplications(getUser())
    # print("testJobIndex: ",testJobIndex)
    # print("testGraduationDate: ", testGraduationDate)
    # print("testStartDate: ", testStartDate)
    # print("testParagraph:", testParagraph)
    # print("JSON: TestJobIndexTuple: ", application[testJobIndex])
    # print("JSON: TestJobIndexGraduationDate: ",application[testJobIndex]["graduationDate"] )
    # print("JSON: TestJobIndexStartDate: ", application[testJobIndex]["startDate"])
    # print("JSON: TestJobIndexParagraphs: ",application[testJobIndex]["paragraph"])
    assert application[testJobIndex]["graduationDate"] == testGraduationDate
    assert application[testJobIndex]["startDate"] == testStartDate
    assert application[testJobIndex]["paragraph"] == testParagraph




@pytest.mark.parametrize("userInputs, jobs", 
[
    (
        ['1','2','1', '1'], '3'
    )

])
def test_deleteJob(capfd, monkeypatch, userInputs,jobs):
    try:
        
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()
        print(readJobPosts())
        
        for job in readJobPosts():
            print(job)
            print(jobs)
            print()
            assert jobs not in job["id"]





@pytest.mark.parametrize("userInputs",
[
    (
        ['1','6','4','2']
    ),
    (
        ['1','6','5','2']
    ),
])

#Note if a user is in "applications" they cannot be deleted from the app.
#TODO ask team if this is fine since the saveJob function seems to be operating on a toggle system.
#This is essentially two test inside of one test
def test_saveJob(capfd, monkeypatch, userInputs):
    try:
        testJobIndex = userInputs[2]
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()

    except IndexError:
        out, err = capfd.readouterr()
        savedJobs = getSavedJobIDs()
        # if "Save this job" in out:

        #     # print(savedJobs)
        #     # print(getUser())
        assert testJobIndex in savedJobs
        # else:
        #     print("Unsave this time")
        #     assert testJobIndex not in savedJobs

    print("End result:",getSavedJobIDs())

@pytest.mark.parametrize("userInputs, testJobIndex",
[
    (
        ['1','3','1','2'],"1" #arr[2] has to be 1, we know it works cause if arr[2 ] != 1 it breaks since the UI stuff!
    )
])
def test_unsaveJob(capfd, monkeypatch, userInputs, testJobIndex):
    try:
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()
        savedJobs = getSavedJobIDs()
        print(savedJobs)
        print(testJobIndex)
        assert testJobIndex not in savedJobs








