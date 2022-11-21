import datetime
from Code.Source.inputAPI import inputMyCollege_jobs, runStudentInputAPI
import pytest
import json
from Code.Source.globalVariables import dataFileInit, getDataFile, getJobFile, getNewJobs, getStudentAccounts, getUser, stackInit, userInit, logout
from Code.Source.loginPrompt import signUpPage
from Code.Source.utility import parseData_newJobs, retrieveAllUsers, writeJson, wJson
from Code.Source.menu import homePage

TESTMODE = True
DATAFILE = 'Code/Data/accounts-test.json'
MESSAGEFILE = 'Code/Data/inbox-test.json'
JOBFILE = 'Code/Data/jobPosts-test.json'

creationTime = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

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
        indexForUser2 = 1
        test_data = data["accounts"][indexForUser2]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
        pytest.profile = {"experience": [], "education": []}
    userInit(pytest.username, pytest.first, pytest.last, "English", email, sms, ads, subscription, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile, "11/01/2022 23:59:59", "11/01/2022 23:59:59")

    open(JOBFILE)
    jobs = {
        "numPosts": 7,
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
            }
        ]
    }
    writeJson(jobs, JOBFILE)

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


#Test Student account input API

#Test the users were created when API is called
def test_studentAPIInput():
    with open(getStudentAccounts(), 'w') as f:
        f.write("user20 random user\nplus\nPassword123*\n=====\nuserTest first last\nstandard\nPassword123!\n=====")
    
    runStudentInputAPI()

    users = retrieveAllUsers()

    assert 'user20' in users
    assert 'userTest' in users

    dataFile = getDataFile()
    
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        
        for users in data["accounts"]:
            if users["username"] == 'user20':
                assert users["firstName"] == 'random'
                assert users["lastName"] == 'user'
                assert users["subscription"] == 'True'
                assert users["password"] == 'Password123*'
            if users["username"] == 'userTest':
                assert users["firstName"] == 'first'
                assert users["lastName"] == 'last'
                assert users["subscription"] == 'False'
                assert users["password"] == 'Password123!'


#Tests if there are the same usernames, it should not register the user
def test_StudentAPIDuplicate():
    with open(getStudentAccounts(), 'w') as f:
        f.write("user20 random user\nplus\nPassword123*\n=====\nuser20 another rando\nstandard\nPassword123!\n=====\nuser7 Johnny Silverhand\nplus\nPassword123*\n=====")

    runStudentInputAPI()

    #Check if both were registered or just the first one since they have the same username
    dataFile = getDataFile()
    
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)
        
        for users in data["accounts"]:
            if users["username"] == 'user20':
                assert users["firstName"] == 'random'
                assert users["lastName"] == 'user' 
            if users["username"] == 'user7':
                assert users["firstName"] != 'Johnny'
                assert users["lastName"] != 'Silverhand'
                assert users["firstName"] == 'Mayank'
                assert users["lastName"] == 'Pandey'
            


# Test Job Input API functionality

#Tests that job Inputs are put into json file
def test_jobAPIInput():
    with open(getNewJobs(), 'w') as f:
        f.write("Professional monkey trainer\nTrains monkeys to do tricks \n&&&\nChau Nguyen\nCircus\nTampa, FL\n$30000\n=====\nProfessional dog trainer\nTrains dogs to do tricks\n&&&\ntommy truong\nCircus\nTampa, FL\n$30000\n=====\n")#Honey badger\nHoney badger don't care\nFor some reason this description is long\nActually it's not that long\nI'm kidding it's long\n&&&\ntommy truong\nSelf-employed\nSomewhere\n$40000\n=====\n")

    #Call API
    newJobs = parseData_newJobs()
    inputMyCollege_jobs(newJobs)

    #Assert that data is in files
    dataFile = getJobFile()
    check1 = False
    check2 = False
    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

        for jobs in data["jobPosts"]:
            if jobs["Title"] == 'Professional monkey trainer':
                check1 = True
                assert jobs["Employer"] == 'Circus'
            if jobs["Title"] == 'Professional dog trainer':
                check2 = True
                assert jobs["Employer"] == 'Circus'

        assert check1 == True
        assert check2 == True

#Test that a job that has the same name as an existing job does not get inputted
def test_jobAPIDuplicates():
    with open(getNewJobs(), 'w') as f:
        f.write("Job3\nWorking is good\n&&&\nSpoopy Ando\nApple\nSilicon Valley\n$300,000\n=====\nProfessional monkey trainer\nTrains monkeys to do tricks \n&&&\nChau Nguyen\nCircus\nTampa, FL\n$30000\n=====\n")

    #Call API
    newJobs = parseData_newJobs()
    inputMyCollege_jobs(newJobs)

    #Assert that job3 is not appended to json file and that monkey trainer is id 8
    dataFile = getJobFile()

    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

        for jobs in data["jobPosts"]:
            if jobs["id"] == '8':
                assert jobs["Title"] == 'Professional monkey trainer'
                assert jobs["Title"] != 'Job3'