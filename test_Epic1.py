import pytest
import random
from Code.Source.utility import securePassword, accountLimit, accountExist
from Code.Source.loginPrompt import register, login, verifyCredentials
from Code.Source.menu import route
from Code.Source.homePageOptions import showHomePageGreeting, showSkillPageGreeting, showConstructionMessage
from Code.Source.globalVariables import stackInit, dataFileInit

TESTMODE = True
DATAFILE =  "Code/Data/accounts-test.json"
ACCOUNT_LIMIT = 10

@pytest.fixture(autouse=True)
def setup():
    open(DATAFILE, 'w').close()
    with open(DATAFILE, 'w') as json_file:
        json_file.write('{"accounts": []}')
    dataFileInit(TESTMODE)

@pytest.fixture
def firstName():
    return "Test"

@pytest.fixture
def lastName():
    return "User"

@pytest.fixture
def username():
    return "test"

@pytest.fixture
def password():
    return "Test123@"

def test_validate_password():
    good_password = "GoodPass123@"
    assert securePassword(good_password) == 1
    bad_passwords = ["pass", "AlmostGoodPasswordButTooLong", "allsmall123@", "HasNoDigit@", "NoSpecChar1"]
    for password in bad_passwords:
        assert securePassword(password) != 1

def test_account_limit(username, password, firstName, lastName):
    assert accountLimit() == 0
    register(username, password, firstName, lastName, False)
    assert accountLimit() == 1

def test_account_exist(username, password, firstName, lastName):
    assert accountExist(username) != 1
    register(username, password, firstName, lastName, False)
    assert accountExist(username) == 1

def test_ten_accounts():
    potential_users = [
        ("test1", "Test123@", "Test1", "User", False),
        ("test2", "Test123@", "Test2", "User", False),
        ("test3", "Test123@", "Test3", "User", False),
        ("test4", "Test123@", "Test4", "User", False),
        ("test5", "Test123@", "Test5", "User", False),
        ("test6", "Test123@", "Test6", "User", False),
        ("test7", "Test123@", "Test7", "User", False),
        ("test8", "Test123@", "Test8", "User", False),
        ("test9", "Test123@", "Test9", "User", False),
        ("test10", "Test123@", "Test10", "User", False)
    ]
    for user in potential_users:
        register(user[0], user[1], user[2], user[3], False)
    assert accountLimit() == ACCOUNT_LIMIT
    bad_user = "test11"
    password = "Test123@"
    first = "Test11"
    last = "User"
    assert register(bad_user, password, first, last, False) != 1
    assert accountLimit() == ACCOUNT_LIMIT

def test_login(username, password, firstName, lastName):
    register(username, password, firstName, lastName, False)
    assert login(username, password) == 1
    bad_username = "bad"
    assert login(bad_username, password) != 1

def test_register_existing_user(username, password, firstName, lastName):
    register(username, password, firstName, lastName, False)
    assert register(username, password, firstName, lastName, False) != 1

def test_register_bad_password(username, password, firstName, lastName):
    password = "bad"
    assert securePassword(password) != 1

def test_login_existing_user(username, password, firstName, lastName):
    register(username, password, firstName, lastName, False)
    assert login(username, password) == 1

    # With invalid password
    bad_password = "bad"
    assert verifyCredentials(username, bad_password) != 1

def test_homePage(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWelcome to InCollege!"
    assert message in out

def test_SkillPage(capfd):
    showSkillPageGreeting()
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nLearn and explore the skill options below!\n1. Communication\n2. Leadership\n3. Collaboration\n4. Responsibility\n5. Time Management\n\nPlease enter a number from 1-5.\nEnter x to return to the home page.\nEnter y to go to previously visited page.\n\n"
    assert out == message

def test_ConstructionMessageJob(capfd):
    showConstructionMessage("Search for a job")
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Search for a job' feature is still under construction.\n\n"
    assert out == message
    
def test_ConstructionMessageFind(capfd):
    showConstructionMessage("Find someone you know")
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Find someone you know' feature is still under construction.\n\n"
    assert out == message

def test_ConstructionMessageSkill(capfd):
    showConstructionMessage("Learn a new skill")
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Learn a new skill' feature is still under construction.\n\n"
    assert out == message

def test_routeFind(capfd):
    stackInit()
    findPage = '2'
    route(findPage)
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Find someone you know' feature is still under construction.\n\n"
    assert out == message