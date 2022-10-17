import pytest
import json
from Code.Source.globalVariables import dataFileInit, getDataFile, getFriendsList, getIncomingRequests, getLoggedUser, getOutgoingRequests, getUser, setFriendsList, setIncomingRequests, setLang, stackInit, userInit
from Code.Source.homePageOptions import showMyNetwork, viewIncomingRequests
from Code.Source.loginPrompt import register
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage, route, usefulLinksMenu
from Code.Source.utility import accountLimit, addToFriendsList, createRequest, getUserFriendList, removeFromFriendsList, removeRequest, storyDisplay

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
    

def test_accountLimit():
    assert accountLimit() <= 10

#Tests if friends list exists and is initialized as an empty container
def test_friendListExist():
    datafile = getDataFile()
    with open(datafile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            assert search["friendsList"] == []

#User1 sends friend request to everyone in the accounts file then all the friend requests are accepted
#Afterwards, user1 removes their entire friendslist and the function tests for that
def test_removeFriend():
    datafile = getDataFile()
    with open(datafile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            recipient_friend = search["username"]
            if recipient_friend == getUser(): continue
            createRequest(getUser(), recipient_friend)
            addToFriendsList(getUser(), recipient_friend)
            removeFromFriendsList(getUser(), recipient_friend)
            assert getFriendsList() == []

#Tests to make sure friend requests are sent
def test_sendFriendRequest():
    datafile = getDataFile()
    with open(datafile) as json_file:
        data = json.load(json_file)
        #Create requests and test request
        for search in data["accounts"]:
            recipient_friend = search["username"]
            if recipient_friend == getUser(): continue
            createRequest(getUser(), recipient_friend)
            assert getOutgoingRequests() != False
        #Cleanup: delete all requests
        for search in data["accounts"]:
            recipient_friend = search["username"]
            if recipient_friend == getUser(): continue
            removeRequest(getUser(), recipient_friend)

#Tests to make sure when user logs on, they can see friend requests
@pytest.mark.parametrize("test_inputs, messages",
[([], "\n\nYou have 1 incoming requests!\n\nIncoming friend requests:\n\n------------------------------------------------------------\n\n\n------------------------------------------------------------\n\nName: Spoopy Ando\nUsername: user2\n\n------------------------------------------------------------\n\nEnter the username of the user you want to select or enter 0 to go to homepage or -1 to exit.\n")])
def test_seeFriendRequest(capsys, monkeypatch, test_inputs, messages):
    try:
        userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', False, False, False, ["user2"])
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        route(7)
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

#Sets a friend list for user and test if that list is returned properly
def test_friendsListRetrieval():
    userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', False, False, False, [], [], ["user2", "testuser1", "testuser3"])
    assert getFriendsList() == ['user2', 'testuser1', 'testuser3']

#Sets outgoing requests for user and tests if that list of outgoing request is returned properly
def test_outgoingRequestRetrieval():
        userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', False, False, False, [], ["user2", "testuser1", "testuser3"], [])
        assert getOutgoingRequests() == ["user2", "testuser1", "testuser3"]

#Each user will have an option to disconnect anyone from their friendlist. If so, remove them from their friends list
@pytest.mark.parametrize('test_inputs, messages',
[([], "My Network:"),
([], "You have 1 friends!\n"),
([], "Enter the username of the user you want to unfriend or enter 0 to go back or -1 to exit.\n")])
def test_disconnectFriend(capsys, monkeypatch, test_inputs, messages):
    try:
        userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', False, False, False, [], [], ["user2"])
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createRequest(getUser(), "user2")
        addToFriendsList(getUser(), "user2")
        showMyNetwork()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out