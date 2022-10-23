import pytest
import json
from Code.Source.homePageOptions import createProfile, displayProfile, showHomePageGreeting, showProfile
from Code.Source.loginPrompt import register
from Code.Source.globalVariables import addPage, dataFileInit, getDataFile, getFirst, getUser, getUserProfile, stackInit, userInit
from Code.Source.menu import homePage
from Code.Source.utility import endProgram

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

# Checks the option is visible
def test_CreateProfileOption(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "10. Create your profile"
    assert message in out

@pytest.mark.parametrize("test_inputs, messages, outputs",
[(['pytest Title', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'y', 'y', 'pytest Job', 'pytest Employer', '01/01/2020',
'01/01/2022', 'pytest Location', 'pytest Description', 'n', 'y', 'pytest School', 'pytest Degree', '2', 'n', '^C'],
["Enter your title:", "Enter your major:", "Enter your university:", "Enter a paragraph about yourself:", "Do you want to add a past job (y/n):",
"Enter title:", "Enter employer:", "Enter date started:", "Enter date ended:", "Enter location:", "Enter Description", "Enter school name:",
"Enter degree", "Enter years attended"], 
["pytest Title", "Pytest Major", "Pytest University", "pytest Paragraph", "pytest Job",
"pytest Employer", "01/01/2020", "01/01/2022", "pytest Location", "pytest Description", "pytest School", "pytest Degree", "2"])])
def test_CreateProfile(capfd, monkeypatch, test_inputs, messages, outputs):
    #Tests creating profile
    try:
        addPage(endProgram)
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createProfile()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

    #Tests that profile is saved
    try:
        profile = getUserProfile()
        name = getFirst()
        displayProfile(profile, name)
    except IndexError:
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
        addPage(endProgram)
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createProfile()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

    #Tests that no experience is showing
    try:
        profile = getUserProfile()
        name = getFirst()
        displayProfile(profile, name)
    except IndexError:
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
        addPage(endProgram)
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createProfile()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out

    #Tests that all three jobs show
    try:
        profile = getUserProfile()
        name = getFirst()
        displayProfile(profile, name)
    except IndexError:
        out, err = capfd.readouterr()
        for output in outputs:
            assert output in out 

@pytest.mark.parametrize("test_inputs, messages",
[(['pytest Title', 'n', 'y', '10', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'n', 'y',
'pytest School', 'pytest Degree', '2', 'n'],
["Enter your title:", "Do you want to continue filling out your profile (y/n):", "Enter your major:"])])
def test_returnToCreateProfile(capfd, monkeypatch, test_inputs, messages):
    #Test that you can return to profile creation after leaving
    try:
        addPage(endProgram)
        addPage(endProgram)
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createProfile()
        createProfile()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out


@pytest.mark.parametrize("test_inputs, messages, inputs2, messages2",
[(['pytest Title', 'y', 'pytest Major', 'y', 'pytest University', 'y', 'pytest Paragraph', 'y', 'y', 'pytest Job', 'pytest Employer', '01/01/2020',
'01/01/2022', 'pytest Location', 'pytest Description', 'n', 'y', 'pytest School', 'pytest Degree', '2', 'n', '^C'],
["Enter your title:", "Enter your major:", "Enter your university:", "Enter a paragraph about yourself:", "Do you want to add a past job (y/n):",
"Enter title:", "Enter employer:", "Enter date started:", "Enter date ended:", "Enter location:", "Enter Description", "Enter school name:",
"Enter degree", "Enter years attended"], 
['2', 'Edited Pytest Title', '8'], ["Enter an option from 2-7 to replace your profile information", "Enter your title:", "Edited Pytest Title"])])
def test_editProfile(capfd, monkeypatch, test_inputs, messages, inputs2, messages2):
    #Creates profile
    try:
        addPage(endProgram)
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        createProfile()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages:
            assert message in out
   
    #Test editing profile
    try:
        addPage(endProgram)
        monkeypatch.setattr('builtins.input', lambda _: inputs2.pop(0))
        showProfile()
    except IndexError:
        out, err = capfd.readouterr()
        for message in messages2:
            assert message in out