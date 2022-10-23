from Code.Source.globalVariables import dataFileInit, getDataFile, getFriendsList, getIncomingRequests, getLoggedUser, getOutgoingRequests, getUser, setFriendsList, setIncomingRequests, setLang, stackInit, userInit
from Code.Source.homePageOptions import showHomePageGreeting, searchUsers, viewIncomingRequests, showMyNetwork
from Code.Source.menu import homePage, route, usefulLinksMenu
from Code.Source.loginPrompt import register
from Code.Source.utility import accountLimit, addToFriendsList, createRequest, getUserFriendList, removeFromFriendsList, removeRequest, storyDisplay, wJson, writeJson
from Code.Source.globalVariables import dataFileInit
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
    register("user1", "Password123!", "Andy", "Nguyen", "University of South Florida", "Computer Science")
    register("user2", "Password123*", "Spoopy", "Ando", "University of Central Florida", "Mechanical Engineering")
    register("testuser1", "Password123@", "tommy", "truong", "Florida State University", "Computer Science")
    register("testuser2", "Password123$", "kevin", "vu", "University of Florida", "Industrial Engineering")

    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        test_data = data["accounts"][0]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
    userInit(pytest.username, pytest.first, pytest.last, "English", True, True, True, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList)

    fileName = getDataFile()
    with open (fileName) as jsonFile:
        data = json.load(jsonFile)
        for users in data["accounts"]:
            if users["username"] == 'testuser1':
                users["outgoingRequests"] = ["testuser2"]
                users["friendsList"] = []
            elif users["username"] == 'testuser2':
                users["incomingRequests"] = ["testuser1"]
                users["friendsList"] = []

    wJson(data, fileName)

#Each user will have the option to disconnect from anyone on their friend list. If so, remove them from each other's lists of friends
@pytest.mark.parametrize("test_inputs, messages",
[(['user1'], ["Enter the username of the user you want to unfriend or enter 0 to go back or -1 to exit."])])
def test_disconnectFriend(capfd, monkeypatch, test_inputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        userInit('user2', 'Spoopy', 'Ando', 'University of Central Florida', 'Mechanical Engineering', 'English', True, True, True, [], [], ["user1"])
        userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', True, True, True, [], [], ["user2"])
        showMyNetwork()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out
        assert [] == getUserFriendList("user1")

#Each user will have a list of friends whom they have connected with (which is initially empty)
@pytest.mark.parametrize("test_inputs, messages",
[([],["My Network:\n\n------------------------------------------------------------\n\nYou have no friends.\n"])])
def test_friendListExist(capfd, monkeypatch, test_inputs, messages):
    monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
    userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', True, True, True, [], [], [])
    showMyNetwork()

    out, err = capfd.readouterr()
    for message in messages:
        assert message in out




