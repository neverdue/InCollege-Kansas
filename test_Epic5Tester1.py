from Code.Source.globalVariables import dataFileInit, getDataFile, getFriendsList, getIncomingRequests, getLoggedUser, getOutgoingRequests, getUser, setFriendsList, setIncomingRequests, setLang, stackInit, userInit
from Code.Source.homePageOptions import showHomePageGreeting, searchUsers, viewIncomingRequests, showMyNetwork
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage, route, usefulLinksMenu
from Code.Source.loginPrompt import register
from Code.Source.utility import accountLimit, addToFriendsList, createRequest, getUserFriendList, removeFromFriendsList, removeRequest, storyDisplay, wJson, writeJson
import pytest
import json

TESTMODE = True
FILENAME = 'Code/Data/jobPosts-test.json'
DATAFILE = 'Code/Data/accounts-test.json'

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    open(DATAFILE, 'w').close()
    with open(DATAFILE, 'w') as json_file:
        json_file.write('{"accounts": []}')

    register("user1", "Password123!", "Andy", "Nguyen")
    register("user2", "Password123*", "Spoopy", "Ando")
    register("testuser1", "Password123@", "tommy", "truong")
    register("testuser2", "Password123$", "kevin", "vu")
    register("user3", "Password123$", "Michael", "vu")
    register("user4", "Password123$", "Tommy", "vu")
    register("user5", "Password123$", "Emily", "vu")
    register("user6", "Password123$", "Michael", "Scott")
    register("user7", "Password123$", "Alex", "vu")
    register("user8", "Password123$", "Emma", "vu")

    profile_template = {
        "experience": [
            {
                "title": "SWE",
                "employer": "Apple",
                "date started": "01/01/2022",
                "date ended": "12/31/2022",
                "location": "California",
                "description": "Software Engineer"
            }
        ],
        "education": [
            {
                "school name": "University of South Florida",
                "degree": "B.S. Computer Science",
                "years attended": "3"
            }
        ],
        "title": "3rd year CS Student ",
        "major": "Computer Science",
        "university": "University Of South Florida",
        "about": "I am {}"
    }

    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        for account in data["accounts"]:
            temp = profile_template.copy()
            temp["about"] = temp["about"].format(account["username"])
            account["profile"] = temp
    wJson(data, DATAFILE)

    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        test_data = data["accounts"][0]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
        pytest.profile = test_data["profile"]
    userInit(pytest.username, pytest.first, pytest.last, "English", True, True, True, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile)

@pytest.mark.parametrize("testInputs, messages", 
[
    (['1', 'user1', 'Password123!', '10', '2'], "I am user1"),
    (['1', 'user2', 'Password123*', '10', '2'], "I am user2"),
    (['1', 'testuser1', 'Password123@', '10', '2'], "I am testuser1"),
    (['1', 'testuser2', 'Password123$', '10', '2'], "I am testuser2"),
    (['1', 'user3', 'Password123$', '10', '2'], "I am user3"),
    (['1', 'user4', 'Password123$', '10', '2'], "I am user4"),
    (['1', 'user5', 'Password123$', '10', '2'], "I am user5"),
    (['1', 'user6', 'Password123$', '10', '2'], "I am user6"),
    (['1', 'user7', 'Password123$', '10', '2'], "I am user7"),
    (['1', 'user8', 'Password123$', '10', '2'], "I am user8")
])
def test_viewMyProfile(capfd, monkeypatch, testInputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: testInputs.pop(0))
        mainPage()
    except IndexError:
        out, err = capfd.readouterr()
        assert messages in out

@pytest.mark.parametrize("friends, message", 
[
    (['user2'], "You have 1 friends"),
    (['user2', 'user5'], "You have 2 friends"),
    (['user2', 'user5', 'user6'], "You have 3 friends"),
    (['testuser1', 'testuser2'], "You have 2 friends"),
    (['testuser1', 'testuser2', 'user2'], "You have 3 friends"),
    (['testuser1', 'testuser2', 'user2', 'user3'], "You have 4 friends"),
    (['testuser1', 'testuser2', 'user2', 'user3', 'user5'], "You have 5 friends"),
    (['testuser1', 'testuser2', 'user2', 'user3', 'user5', 'user6'], "You have 6 friends")
])
def test_showMyNetwork(capfd, friends, message):
    try:
        for user in friends:
            createRequest(pytest.username, user)
            addToFriendsList(pytest.username, user)
        showMyNetwork()
    except OSError:
        out, err = capfd.readouterr()
        assert message in out

@pytest.mark.parametrize("testInputs, friends, messages", 
[
    # FORMAT ---------> input to the program, friends list, expected output
    (
        ['1', 'user1', 'Password123!', '9', 'user2', '1'], 
        ['user2'], 
        ["I am user2"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'user2', '1', '0', '9', 'user5', '1'], 
        ['user2', 'user5'], 
        ["I am user2", "I am user5"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'user2', '1', '0', '9', 'user5', '1', '0', '9', 'user6', '1'], 
        ['user2', 'user5', 'user6'], 
        ["I am user2", "I am user5", "I am user6"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'testuser1', '1', '0', '9', 'testuser2', '1'], 
        ['testuser1', 'testuser2'], 
        ["I am testuser1", "I am testuser2"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'testuser1', '1', '0', '9', 'testuser2', '1', '0', '9', 'user2', '1'], 
        ['testuser1', 'testuser2', 'user2'], 
        ["I am testuser1", "I am testuser2", "I am user2"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'testuser1', '1', '0', '9', 'testuser2', '1', '0', '9', 'user2', '1', '0', '9', 'user3', '1'], 
        ['testuser1', 'testuser2', 'user2', 'user3'], 
        ["I am testuser1", "I am testuser2", "I am user2", "I am user3"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'testuser1', '1', '0', '9', 'testuser2', '1', '0', '9', 'user2', '1', '0', '9', 'user3', '1', '0', '9', 'user5', '1'], 
        ['testuser1', 'testuser2', 'user2', 'user3', 'user5'], 
        ["I am testuser1", "I am testuser2", "I am user2", "I am user3", "I am user5"]
    ),
    (
        ['1', 'user1', 'Password123!', '9', 'testuser1', '1', '0', '9', 'testuser2', '1', '0', '9', 'user2', '1', '0', '9', 'user3', '1', '0', '9', 'user5', '1', '0', '9', 'user6', '1'], 
        ['testuser1', 'testuser2', 'user2', 'user3', 'user5', 'user6'], 
        ["I am testuser1", "I am testuser2", "I am user2", "I am user3", "I am user5", "I am user6"]
    )
])
def test_viewMyFriendsProfile(capfd, monkeypatch, testInputs, friends, messages):
    try:
        for user in friends:
            createRequest(pytest.username, user)
            addToFriendsList(pytest.username, user)
        monkeypatch.setattr('builtins.input', lambda _: testInputs.pop(0))
        mainPage()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out