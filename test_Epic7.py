import pytest
import json
from io import StringIO
from Code.Source.globalVariables import dataFileInit, getUser, stackInit, userInit, logout
from Code.Source.loginPrompt import signUpPage
from Code.Source.utility import writeJson, wJson
from Code.Source.menu import homePage

TESTMODE = True
DATAFILE = 'Code/Data/accounts-test.json'
MESSAGEFILE = 'Code/Data/inbox-test.json'

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

    open(MESSAGEFILE)
    messageJson = {
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
                "user2" : [

                    "this is a message from testuser1, a subscribed person to user2"
                ]
            }
        },
        "incoming": {
            "user2": {
                "user1": [
                    "this is a message from user 1 to user2",
                    "pytest user2 and user1"
                ],
                "testuser1" : ["this is a message from testuser1, a subscribed person to user2"]
            },
            "testuser2": {
                "testuser1": [
                    "testing message from testuser1 to testuser2"
                ]
            },
            "user1": {
                "user2":[
                    
                ]
            }
        }
    }
    writeJson(messageJson, MESSAGEFILE)

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

@pytest.mark.parametrize("subscription_inputs, subscription_info, billing_message", 
[("yes\n", "True", "We will start to bill you $10 monthly. Thank you for becoming a PLUS member!"), 
("no\n", "False", "")])
def test_subscriptionOption(capsys, monkeypatch, subscription_inputs, subscription_info, billing_message):
    logout()
    data = json.load(open(DATAFILE))
    wJson({"accounts": []}, DATAFILE) # Have to overwrite accounts-test.json else cannot register due to account limit

    # TEST: subscription option is shown with billing message when user registers for new account
    test_inputs = "ctrbl\nPassword123!\nChau\nNguyen\n"
    message = "Would you like to subscribe to become a plus member for $10 a month?\n\t*As a plus member you can send and receive messages from anyone in the InCollege system*\n\t\t\t*rather than only users you are friends with*\n(yes/no):"
    monkeypatch.setattr("sys.stdin", StringIO(test_inputs + subscription_inputs)) 
    signUpPage()
    out, err = capsys.readouterr()
    assert message in out 
    assert billing_message in out 

    # TEST: registered subscription info is stored correctly along with account info
    temp_data = json.load(open(DATAFILE))
    assert subscription_info == temp_data["accounts"][0]["subscription"]

    wJson(data, DATAFILE)

@pytest.mark.parametrize("userInputs, messageIndex",
[
    (
        ['11','2', 'user1'], 0
    )
]

)
def test_showRecievedMessages(monkeypatch, capfd, userInputs, messageIndex):
    try:
        viewedMessageSender = userInputs[2]
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()
    with open(MESSAGEFILE) as message_file:
        data = json.load(message_file)
        print(data["incoming"][getUser()][viewedMessageSender][messageIndex])
        assert data["incoming"][getUser()][viewedMessageSender][messageIndex] in out
        #Ask about this implementation



@pytest.mark.parametrize("userInputs",
[
    (
        ['11','1', 'user1', 'pytest message from user 2 to user 1']
    )
]
)
def test_storeSentMessagesToReceiver(monkeypatch, capfd, userInputs):
    try:
        userSentTo = userInputs[2]
        messageSent = userInputs[3]
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()

    with open(MESSAGEFILE) as message_file:
        data = json.load(message_file)
        print(messageSent)
        print(data["incoming"][userSentTo][getUser()]
)
        assert messageSent in data["incoming"][userSentTo][getUser()]
                

@pytest.mark.parametrize("userInputs",
[
    (
        ['11','2', 'user1','1','pytest REPLY message from user 2 to user 1']
    )
]
)
def test_replyToUser(monkeypatch, capfd, userInputs):
    try:
        userSentTo = userInputs[2]
        messageSent = userInputs[4]
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()

    with open(MESSAGEFILE) as message_file:
        data = json.load(message_file)
        print(messageSent)
        print(data["incoming"][userSentTo][getUser()])
        assert messageSent in data["incoming"][userSentTo][getUser()]


#MESSAGE INDEX MUST MATCH userInputs[4] - 1
#wanted to bring up scoping issues i had earlier with the print statement
@pytest.mark.parametrize("userInputs, messageIndex",
[
    (
        ['11','2', 'user1','2','1'], 0
    ),
    (
        ['11','2', 'user1','2','2'], 1


    )
]
)
def test_deleteMessage(monkeypatch, capfd, userInputs, messageIndex):
    try:
        user = userInputs[2]
        with open(MESSAGEFILE) as message_file:
            data = json.load(message_file)
            messageToDelete = data["incoming"][getUser()][user][messageIndex]
            #a print statement wont print in here
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))

        homePage()
    except IndexError:
        out, err = capfd.readouterr()
        print("What is in JSON before delete: ",data["incoming"][getUser()][user])
       
    with open(MESSAGEFILE) as message_file:
        data = json.load(message_file)
        print("What is in JSON after delete: ",data["incoming"][getUser()][user])
        print("Message designated to be deleted: ", messageToDelete)
        assert messageToDelete not in data["incoming"][getUser()][user]

def test_notifyNewMessages(capfd):
    try:
        homePage()
    except OSError:
        
        out,err  = capfd.readouterr()
        assert "You have messages" in out

        #not viable since not an efficient way of telling, just printing based off of what we expect from this user
                # with open(MESSAGEFILE) as message_file:
                #     data = json.load(message_file)
                #     if(len(data["incoming"][getUser()]) > 0):
                #         assert "You have messages" in out
                #     else:
                #         assert "You have messages" not in out
@pytest.mark.parametrize("userInputs, messageIndex",
[
    (
    ['11','2', 'testuser1', '1'], 0
    )
]

)
def test_subscriptionMessagePermissions(monkeypatch, capfd, userInputs, messageIndex):
    try:
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()
        # print(out)
    assert "I'm sorry, you are not friends with that person" in out


#TODO test_plusUsersSendEveryone - if not frien
# 
#d


@pytest.mark.parametrize("userInputs",
[
    (
    ['11','1', 'user2', 'Pytest: I am a recruiter(plus member) messaging a standard user named user2']
    )
]

)
def test_plusUsersSendEveryone(monkeypatch, capfd, userInputs):
    email = True
    sms = True
    ads = True
    subscription = True
    with open(DATAFILE, 'r') as json_file:
        data = json.load(json_file)
        #using index1
        indexForTestuser1 = 2
        test_data = data["accounts"][indexForTestuser1]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
        pytest.incomingRequests = test_data["incomingRequests"]
        pytest.outgoingRequests = test_data["outgoingRequests"]
        pytest.friendsList = test_data["friendsList"]
        pytest.profile = {"experience": [], "education": []}
        userInit(pytest.username, pytest.first, pytest.last, "English", email, sms, ads, subscription, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile, "11/01/2022 23:59:59", "11/01/2022 23:59:59")
    try:
        standardAccountReceiver = userInputs[2]
        messageSent = userInputs[3]
        monkeypatch.setattr('builtins.input', lambda _: userInputs.pop(0))
        homePage()
    except IndexError:
        out, err = capfd.readouterr()
        print(out)
    with open(MESSAGEFILE) as message_file:
            data = json.load(message_file)
            print(messageSent)
            print(getUser())
            print(data["incoming"][standardAccountReceiver][getUser()])
            assert messageSent in data["incoming"][standardAccountReceiver][getUser()]

