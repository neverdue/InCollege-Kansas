from Code.Source.globalVariables import dataFileInit, getDataFile, getFriendsList, getIncomingRequests, getLoggedUser, getOutgoingRequests, getUser, setFriendsList, setIncomingRequests, setLang, stackInit, userInit
from Code.Source.homePageOptions import showHomePageGreeting, searchUsers, viewIncomingRequests, showMyNetwork
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
    register("user1", "Password123!", "Andy", "Nguyen", False)
    register("user2", "Password123*", "Spoopy", "Ando", False)
    register("testuser1", "Password123@", "tommy", "truong", False)
    register("testuser2", "Password123$", "kevin", "vu", False)

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
        

def test_IncomingRequestOption(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "See Incoming Friend Requests"
    assert message in out

def test_outgoingRequestOption(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "See Outgoing Friend Requests"
    assert message in out

@pytest.mark.parametrize("test_inputs, messages",
[(['1', 'Ando'], ["Search by last name", "Enter the username of the user you want to send a friend request."])])
def test_searchLastName(capfd, monkeypatch, test_inputs, messages):
    try:
        inputs = iter(['1', 'Ando'])
        monkeypatch.setattr('builtins.input', lambda _: test_inputs[0])
        searchUsers()
    except IndexError:
        out, err = capfd.readouterr()
        assert messages in out 

@pytest.mark.parametrize("test_inputs, messages",
[(['2', 'Mechanical Engineering'], ["Search by Major", "Enter the major of the user you want to send a friend request."])])
def test_searchMajor(capfd, monkeypatch, test_inputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs[0])
        searchUsers()
    except IndexError:
        out, err = capfd.readouterr()
        assert messages in out 


@pytest.mark.parametrize("test_inputs, messages",
[(['3', 'University of Central Florida'], ["Search by university", "Enter the university of the user you are looking for."])])
def test_searchUniversity(capfd, monkeypatch, test_inputs, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs[0])
        searchUsers()
    except IndexError:
        out, err = capfd.readouterr()
        assert messages in out 

def test_RequestNotification(capfd):
    userInit('user1', 'Andy', 'Nguyen', 'English', True, True, True, False, ["user2"], [], [], {"experience": {}, "education": {}})
    try:
        homePage()
    except OSError:
        out, err = capfd.readouterr()
        assert "You have 1 incoming friend request" in out

@pytest.mark.parametrize("test_input, messages",
[(['testuser1', '1'], ["You have 1 incoming request", "1. Accept\n2. Decline"])])
def test_AcceptFriendRequest(capfd, monkeypatch, test_input, messages):
    try:
        monkeypatch.setattr('builtins.input', lambda _: test_input.pop(0))
        
        #Get user info from json
        dataFile = getDataFile()
        with open(dataFile, "r") as json_file:
            data = json.load(json_file)
            for items in data["accounts"]:
                tempUser = items["username"]
                if 'testuser2' == tempUser:
                    firstname = items["firstName"]
                    lastname = items["lastName"]
                    incomingRequests = items["incomingRequests"]
                    outgoingRequests = items["outgoingRequests"]
                    friendsList = items["friendsList"]
                    language = "English" if items["language"] == "English" else "Spanish"
                    email = True if items["email"] == "True" else False
                    SMS = True if items["SMS"] == "True" else False 
                    ads = True if items["ads"] == "True" else False

        #set user variable
        userInit('testuser2', firstname, lastname, language, email, SMS, ads, False, incomingRequests, outgoingRequests, friendsList)
        viewIncomingRequests()

    except IndexError:
        assert "testuser1" in getFriendsList()
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out
                 

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
[([], "\n\nYou have 1 incoming request!\n\nIncoming friend requests:\n\n------------------------------------------------------------\n\n\n------------------------------------------------------------\n\nName: Spoopy Ando\nUsername: user2\n\n------------------------------------------------------------\n\nEnter the username of the user you want to select or enter 0 to go to homepage or -1 to exit.\n")])
def test_seeFriendRequest(capsys, monkeypatch, test_inputs, messages):
    try:
        userInit('user1', 'Andy', 'Nguyen', 'English', False, False, False, False, ["user2"])
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        route(7)
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

#Sets a friend list for user and test if that list is returned properly
def test_friendsListRetrieval():
    userInit('user1', 'Andy', 'Nguyen', 'English', False, False, False, False, [], [], ["user2", "testuser1", "testuser3"])
    assert getFriendsList() == ['user2', 'testuser1', 'testuser3']

#Sets outgoing requests for user and tests if that list of outgoing request is returned properly
def test_outgoingRequestRetrieval():
        userInit('user1', 'Andy', 'Nguyen', 'English', False, False, False, False, [], ["user2", "testuser1", "testuser3"], [])
        assert getOutgoingRequests() == ["user2", "testuser1", "testuser3"]

#Each user will have an option to disconnect anyone from their friendlist. If so, remove them from their friends list
@pytest.mark.parametrize('test_inputs, messages',
[([], "My Network:"),
([], "You have 1 friends!\n"),
([], "Name: Spoopy Ando\n")])
def test_disconnectFriend(capsys, monkeypatch, test_inputs, messages):
    try:
        userInit('user1', 'Andy', 'Nguyen', 'English', False, False, False, False, [], [], ["user2"])
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createRequest(getUser(), "user2")
        addToFriendsList(getUser(), "user2")
        showMyNetwork()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out