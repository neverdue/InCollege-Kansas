import json
from Code.Source.utility import writeJson
import pytest
from unittest.mock import patch
from Code.Source import globalVariables
from Code.Source.globalVariables import addPage, dataFileInit, getDataFile, getEmailPref, getLang, getUser, removePage, stackInit, userInit, logout
from Code.Source.mainPage import mainPage
from Code.Source.menu import usefulLinksMenu, incollegeImpLinks
from Code.Source.menuOptions import back, general, guestControls, helpCenter, about, press, blog, careers, developers, browseInCollege, businessSolutions, directories, privacyPolicy
from Code.Source.menuOptions import copyrightNotice, accessibility, userAgreement, cookiePolicy, copyrightPolicy, brandPolicy, languages

TESTMODE = True 
NO_INPUT = OSError

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', True, True, True)

# # Test: Link options available before and after user signed in 
@pytest.mark.parametrize('login', [0, 1])
def test_links(capsys, monkeypatch, login):
    try: 
        if not login:
            logout()
        mainPage()
    except NO_INPUT:
        out, err = capsys.readouterr()
        assert 'Useful Links' in out 
        assert 'InCollege Important Links' in out

# Test: Useful Links display appropriate links 
def test_usefulLinksMenu(capsys, monkeypatch): 
    links = ['General', 'Browse InCollege', 'Business Solutions', 'Directories']
    try: 
        usefulLinksMenu()
    except NO_INPUT: 
        out, err = capsys.readouterr()
        for link in links:
            assert link in out 

# Test: Sign up will direct to sign in processing section
@patch('Code.Source.menuOptions.signUpPage')
def test_sign_up(sign_up_mock, monkeypatch): 
    logout()    
    monkeypatch.setattr('builtins.input', lambda _: '1') # Select Sign Up option
    general()
    sign_up_mock.assert_called() # Test if mock function was called 

# Test: General display appropriate links
def test_general(capsys, monkeypatch): 
    links = ['Sign Up', 'Help Center', 'About', 'Press', 'Blog', 'Careers', 'Developers']
    try: 
        general()   
    except NO_INPUT: 
        out, err = capsys.readouterr()
        for link in links:
            assert link in out

# Test: Following functions display 'Under construction' message
@pytest.mark.parametrize('function', [blog, careers, developers, browseInCollege, businessSolutions, directories])
def test_under_construction(capsys, function):
    try:
        function()
    except NO_INPUT:
        message = 'Under construction'
        out, err = capsys.readouterr()
        assert message in out 

# Test: InCollege Important Links display appropriate links
def test_incollegeImpLinks(capsys, monkeypatch):
    links = ['Copyright Notice', 'About', 'Accessibility', 'User Agreement', 'Privacy Policy', 
    'Cookie Policy', 'Copyright Policy', 'Brand Policy', 'Languages']
    try: 
        incollegeImpLinks()
    except NO_INPUT:
        out, err = capsys.readouterr()
        for link in links:
            assert link in out 

# Test: Following functions display appropriate messages 
@pytest.mark.parametrize('function, message',
[(helpCenter, "We're here to help"),
(about, "In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide"),
(press, 'In College Pressroom: Stay on top of the latest news, updates, and reports'),
(copyrightNotice, 'Copyright Notice'), (accessibility, 'accessibility'), (userAgreement, 'User Agreement'),
(privacyPolicy, 'Guest Controls'), (cookiePolicy, 'cookie policy'), (copyrightPolicy, 'copyright policy'),
(brandPolicy, 'Brand Policy'), (languages, 'English'), (languages, 'Spanish')])

def test_important_links_message(capsys, function, message):
    try: 
        function()   
    except NO_INPUT: 
        out, err = capsys.readouterr()
        assert message in out

# Test: Ensure signed in users are shown options to adjust email, sms, and ads features in Privacy Policy -> Guest Controls
def test_guest_controls(capsys, monkeypatch):
    try: 
        guestControls()
    except NO_INPUT:
        out, err = capsys.readouterr()
        assert 'Would you like to update any of your settings' in out 
        assert 'Update emails(1), SMS(2), ads(3)' in out 

# IC-24 Make sure all new pages are functional with the page stack
def test_general():
    #Testing add and removal of general page and subpages of general
    #Only option is to go forward 1 page then back to general

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
    #Test if removing empty stack doesn't break program
    assert removePage() == []

    #Remove page pops 2; testing if removing 2 items from a stack of 1 item breaks program
    addPage(general)
    assert removePage() == globalVariables.pageStack

# IC-27 For language localization, when the setting is changed, update the user object in JSON.
def test_language_localization():
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
    #We have no idea why, but i need to either have userInity as a global or contained in here
    #Otherwise it doesn't work
    userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', True, True, True)
    #Email, SMS, ads are either all on or off. Function helps decide which pytest to test for
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

def test_guestControls(capsys, monkeypatch, test_inputs, messages):
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

def test_guestControls2(capsys, monkeypatch, test_inputs2, messages):
    try:
        userInit('user1', 'Andy', 'Nguyen', 'University of South Florida', 'Computer Science', 'English', False, False, False)
        monkeypatch.setattr('builtins.input', lambda _: test_inputs2.pop(0))
        guestControls()
    except IndexError:
        out, err = capsys.readouterr()
        assert messages in out