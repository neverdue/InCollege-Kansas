import pytest
from unittest.mock import patch
from Code.Source.globalVariables import dataFileInit, stackInit, userInit, logout
from Code.Source.mainPage import mainPage
from Code.Source.menu import usefulLinksMenu, incollegeImpLinks
from Code.Source.menuOptions import general, guestControls, helpCenter, about, press, blog, careers, developers, browseInCollege, businessSolutions, directories, privacyPolicy
from Code.Source.menuOptions import copyrightNotice, accessibility, userAgreement, cookiePolicy, copyrightPolicy, brandPolicy, languages

TESTMODE = True 
NO_INPUT = OSError

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()
    userInit('user1', 'Andy', 'Nguyen', 'English', True, True, True)

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