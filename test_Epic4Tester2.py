import pytest
import json
from Code.Source.globalVariables import dataFileInit, getDataFile, getFriendsList, getUser, stackInit, userInit
from Code.Source.utility import accountLimit, addToFriendsList, createRequest, removeFromFriendsList, removeRequest

TESTMODE = True 
NO_INPUT = OSError

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', True, True, True)

def test_accountLimit():
    assert accountLimit() <= 10

def test_removeFriend(capfd):
    out, err = capfd.readouterr()
    datafile = getDataFile()
    message = "Unfriended!"
    with open(datafile) as json_file:
        data = json.load(json_file)
        for search in data["accounts"]:
            recipient_friend = search["username"]
            if recipient_friend == getUser(): continue
            createRequest(getUser(), recipient_friend)
            addToFriendsList(getUser(), recipient_friend)
            removeFromFriendsList(getUser(), recipient_friend)
            assert getFriendsList() == []

    


#pytest test_Epic4Tester2.py -rP