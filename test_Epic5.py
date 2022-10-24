from Code.Source.globalVariables import addPage, dataFileInit, getFirst, getUserProfile, stackInit, userInit
from Code.Source.homePageOptions import createProfile, displayProfile, showHomePageGreeting, showProfile, showMyNetwork
from Code.Source.mainPage import mainPage
from Code.Source.menu import homePage
from Code.Source.loginPrompt import register
from Code.Source.utility import addToFriendsList, createRequest, terminateProgram,  wJson
import io
import pytest
import json

TESTMODE = True
FILENAME = 'Code/Data/jobPosts-test.json'
DATAFILE = 'Code/Data/accounts-test.json'

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    addPage(homePage)
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
            account["profile"] = {"experience": [], "education": []} if account["username"] == "user1" else temp
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
        pytest.profile = {"experience": [], "education": []}
    userInit(pytest.username, pytest.first, pytest.last, "English", True, True, True, pytest.incomingRequests, pytest.outgoingRequests, pytest.friendsList, pytest.profile)

@pytest.mark.parametrize("testInputs, messages", 
[
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


# Checks the option is visible
def test_CreateProfileOption(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "10. Your profile"
    assert message in out

@pytest.mark.parametrize("test_inputs, messages, outputs",
[(['pytest Title', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'y', 'y', 'pytest Job', 'pytest Employer', '01/01/2020',
'01/01/2022', 'pytest Location', 'pytest Description', 'n', 'y', 'pytest School', 'pytest Degree', '2', 'n'],
["Enter your title:", "Enter your major:", "Enter your university:", "Enter a paragraph about yourself:", "Do you want to add a past job (y/n):",
"Enter title:", "Enter employer:", "Enter date started:", "Enter date ended:", "Enter location:", "Enter description", "Enter school name:",
"Enter degree", "Enter years attended"], 
["pytest Title", "Pytest Major", "Pytest University", "pytest Paragraph", "pytest Job",
"pytest Employer", "01/01/2020", "01/01/2022", "pytest Location", "pytest Description", "pytest School", "pytest Degree", "2"])])
def test_CreateProfile(capfd, monkeypatch, test_inputs, messages, outputs):
    #Tests creating profile
    try:
        addPage(terminateProgram)
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(test_inputs)))
        createProfile()
    except EOFError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out 

    #Tests that profile is saved
    profile = getUserProfile()
    name = getFirst()
    displayProfile(profile, name)
    out, err = capfd.readouterr()
    for output in outputs:
        assert output in out 

@pytest.mark.parametrize("test_inputs, messages, outputs",
[(['pytest Title', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'y', 'n', 'y', 
'pytest School', 'pytest Degree', '2', 'n'],
["Do you want to add a past job (y/n):", "Enter school name:", "Enter degree", "Enter years attended"], 
["6. Experience:\n\n7. Education:"])])
def test_optionalExperience(capfd, monkeypatch, test_inputs, messages, outputs):
    try:
        addPage(terminateProgram)
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(test_inputs)))
        createProfile()
    except EOFError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

    #Tests that no experience is showing
    profile = getUserProfile()
    name = getFirst()
    displayProfile(profile, name)
    out, err = capfd.readouterr()
    for output in outputs:
        assert output in out 

@pytest.mark.parametrize("test_inputs, messages, outputs",
[(['pytest Title', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'y', 'y', 'pytest Job1', 'pytest Employer1', '01/01/2020',
'01/01/2022', 'pytest Location1', 'pytest Description1', 'y', 'pytest Job2', 'pytest Employer2', '01/01/2018',
'01/01/2020', 'pytest Location2', 'pytest Description2', 'y', 'pytest Job3', 'pytest Employer3', '01/01/2016',
'01/01/2017', 'pytest Location3', 'pytest Description3', 'y', 'pytest School', 'pytest Degree', '2', 'n'],
["Do you want to add a past job (y/n):", "The limit for past job experiences have been reached"],
["pytest Job1", "pytest Job2", "pytest Job3"])])
def test_maxExperience(capfd, monkeypatch, test_inputs, messages, outputs):
    try:
        addPage(terminateProgram)
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(test_inputs)))
        createProfile()
    except EOFError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

    #Tests that all three jobs show
    profile = getUserProfile()
    name = getFirst()
    displayProfile(profile, name)
    out, err = capfd.readouterr()
    for output in outputs:
        assert output in out 

@pytest.mark.parametrize("test_inputs, messages, outputs",
[(['pytest Title', 'n', '10', '1', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'n', '10', '1', 'n', 'y', 'pytest School', 'pytest Degree', '2', 'n'],
["Enter your title:", "Do you want to continue filling out your profile (y/n):", "Enter your major:"],
['pytest Title', 'Pytest Major', 'Pytest University', 'pytest Paragraph', 'pytest School', 'pytest Degree', '2'])])
def test_returnToCreateProfile(capfd, monkeypatch, test_inputs, messages, outputs):
    #Test that you can return to profile creation after leaving
    try:
        addPage(homePage)
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(test_inputs)))
        createProfile()
    except EOFError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

    #Test profile is saved
    profile = getUserProfile()
    name = getFirst()
    displayProfile(profile, name)
    out, err = capfd.readouterr()
    for output in outputs:
        assert output in out 

@pytest.mark.parametrize("test_inputs, messages, inputs2, messages2",
[(['pytest Title', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'y', 'y', 'pytest Job', 'pytest Employer', '01/01/2020',
'01/01/2022', 'pytest Location', 'pytest Description', 'n', 'y', 'pytest School', 'pytest Degree', '2', 'n'],
["Enter your title:", "Enter your major:", "Enter your university:", "Enter a paragraph about yourself:", "Do you want to add a past job (y/n):",
"Enter title:", "Enter employer:", "Enter date started:", "Enter date ended:", "Enter location:", "Enter description", "Enter school name:",
"Enter degree", "Enter years attended"], 
['2', 'Edited Pytest Title', '8'], ["Enter an option from 2-7 to replace your profile information", "Enter your title:", "Edited Pytest Title"])])
def test_editProfile(capfd, monkeypatch, test_inputs, messages, inputs2, messages2):
    #Creates profile
    try:
        addPage(terminateProgram)
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(test_inputs)))
        createProfile()
    except EOFError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out
   
    #Test editing profile
    try:
        addPage(terminateProgram)
        monkeypatch.setattr('sys.stdin', io.StringIO('\n'.join(inputs2)))
        showProfile()
    except EOFError:
        out, err = capfd.readouterr()
        for message in messages2:
            assert message in out