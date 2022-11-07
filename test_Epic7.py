import pytest
import json
from io import StringIO
from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUser, getUserProfile, stackInit, userInit, logout
from Code.Source.loginPrompt import signUpPage
from Code.Source.utility import writeJson, wJson
from Code.Source.mainPage import mainPage
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
    userInit(pytest.username, pytest.first, pytest.last, "English", email, sms, ads, subscription, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile)

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
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": ["user2"],
        "profile": {
            "experience": [
            {
                "title": "pytest Job",
                "employer": "pytest Employer",
                "date started": "01/01/2020",
                "date ended": "01/01/2022",
                "location": "pytest Location",
                "description": "pytest Description"
            }
            ],
            "education": [
            {
                "school name": "pytest School",
                "degree": "pytest Degree",
                "years attended": "2"
            }
            ],
            "title": "Edited Pytest Title",
            "major": "Pytest Major",
            "university": "Pytest University",
            "about": "pytest Paragraph"
        }
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
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": ["user1"],
        "profile": {
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
            "about": "I am user2"
        }
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
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am testuser1"
        }
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
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am testuser2"
        }
        },
        {
        "username": "user3",
        "password": "Password123$",
        "firstName": "Michael",
        "lastName": "vu",
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am user3"
        }
        },
        {
        "username": "user4",
        "password": "Password123$",
        "firstName": "Tommy",
        "lastName": "vu",
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am user4"
        }
        },
        {
        "username": "user5",
        "password": "Password123$",
        "firstName": "Emily",
        "lastName": "vu",
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am user5"
        }
        },
        {
        "username": "user6",
        "password": "Password123$",
        "firstName": "Michael",
        "lastName": "Scott",
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am user6"
        }
        },
        {
        "username": "user7",
        "password": "Password123$",
        "firstName": "Alex",
        "lastName": "vu",
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am user7"
        }
        },
        {
        "username": "user8",
        "password": "Password123$",
        "firstName": "Emma",
        "lastName": "vu",
        "language": "English",
        "email": "True",
        "SMS": "True",
        "ads": "True",
        "subscription": "False",
        "incomingRequests": [],
        "outgoingRequests": [],
        "friendsList": [],
        "profile": {
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
            "about": "I am user8"
        }
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
        userInit(pytest.username, pytest.first, pytest.last, "English", email, sms, ads, subscription, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile)
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

