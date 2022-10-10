import pytest
import json

#Have to include this otherwise i won't be able to use the pageStack
from Code.Source import globalVariables

from Code.Source.utility import writeJson
from Code.Source.globalVariables import stackInit, addPage, removePage, dataFileInit, getDataFile, getUser, getLang, getEmailPref
from Code.Source.menuOptions import general, helpCenter, about, press, blog, careers, developers, back, guestControls
from Code.Source.loginPrompt import login

@pytest.fixture(autouse=True)
# IC-24 Make sure all new pages are functional with the page stack
def test_general():
    #Testing add and removal of general page and subpages of general
    #Only option is to go forward 1 page then back to general
    stackInit()

    #Testing page traversal (adding to stack)
    addPage(general)
    assert globalVariables.pageStack == [general]

    addPage(helpCenter)
    assert globalVariables.pageStack == [general, helpCenter]

    #Testing page removal
    assert removePage() == general

    #Testing the rest of the pages
    addPage(general)
    addPage(about)
    assert globalVariables.pageStack == [general, about]

    addPage(removePage())
    addPage(press)
    assert globalVariables.pageStack == [general, press]

    addPage(removePage())
    addPage(blog)
    assert globalVariables.pageStack == [general, blog]

    addPage(removePage())
    addPage(careers)
    assert globalVariables.pageStack == [general, careers]

    addPage(removePage())
    addPage(developers)
    assert globalVariables.pageStack == [general, developers]

    addPage(removePage())
    addPage(back)
    assert globalVariables.pageStack == [general, back]

def test_general_empty_stack():
    stackInit()

    #Test if removing empty stack doesn't break program
    assert removePage() == []

    #Remove page pops 2; testing if removing 2 items from a stack of 1 item breaks program
    addPage(general)
    assert removePage() == globalVariables.pageStack

# IC-27 For language localization, when the setting is changed, update the user object in JSON.
def test_language_localization():
    #Check from testing JSON file
    dataFileInit(True)

    #Login to existing user
    login("user2", "Password123*")

    #Always changes the language of user2 and checks if it does
    file = getDataFile()
    with open(file) as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            if(getUser() == user):
                if getLang() == "English":
                    items["language"] = "Spanish"
                    lang_switch = 1
                elif getLang() == "Spanish":
                    items["language"] = "English"
                    lang_switch = 1

    writeJson(data, file)
    assert lang_switch == 1

#Helper function to test GuestControl features (IC-26)
def getStatus():
    #Email, SMS, ads are either all on or off. Function helps decide which pytest to test for
    stackInit()
    dataFileInit(True)
    login("user1", "Password123!")
    if(getEmailPref() == True):
        return "True"
    elif(getEmailPref() == False):
        return "False"

# IC-26 Update the User object to hold the "GuestControls" features.
#Tests case for when need to check if GuestControl features are turned off
@pytest.mark.parametrize("test_inputs, messages",
[(['1'], "\nYou will no longer receive emails from InCollege.\n"),
(['2'], "\nYou will no longer receive SMS messages from InCollege.\n"),
(['3'], "\nYou will no longer receive targeted ads.\n")])

@pytest.mark.skipif(getStatus() == "False", reason="Skipping this test function because test JSON needs to be tested from false guest control values to true")
def test_guestControls(capsys, monkeypatch, test_inputs, messages):
    stackInit()
    dataFileInit(True)
    login("user1", "Password123!")

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
        guestControls()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out

# IC-26 Update the User object to hold the "GuestControls" features.
#Tests case for when need to check if GuestControl features are turned on
@pytest.mark.parametrize("test_inputs2, messages",
[(['1'], "\nYou will now receive emails from InCollege.\n"),
(['2'], "\nYou will now receive SMS messages from InCollege.\n"),
(['3'], "\nYou will now receive targeted ads.\n")])

@pytest.mark.skipif(getStatus() == "True", reason="Skipping this test function because test JSON needs to be tested from true guest control values to negative")
def test_guestControls2(capsys, monkeypatch, test_inputs2, messages):
    stackInit()
    dataFileInit(True)
    login("user1", "Password123!")

    try:
        monkeypatch.setattr('builtins.input', lambda _: test_inputs2.pop(0))
        guestControls()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out


    
