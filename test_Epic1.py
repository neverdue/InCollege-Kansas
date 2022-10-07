import pytest
from Code.Source.utility import securePassword, accountLimit, accountExist
from Code.Source.loginPrompt import register, login, verifyCredentials
from Code.Source.menu import route
from Code.Source.homePageOptions import showHomePageGreeting, showSkillPageGreeting, showConstructionMessage
from Code.Source.globalVariables import stackInit, dataFileInit

TESTMODE = True
DATAFILE =  "Code/Data/accounts-test.json"

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
    register(username, password, firstName, lastName)
    assert accountLimit() == 1

def test_account_exist(username, password, firstName, lastName):
    assert accountExist(username) != 1
    register(username, password, firstName, lastName)
    assert accountExist(username) == 1

def test_five_accounts():
    potential_users = [
        ("test1", "Test123@", "Test1", "User"),
        ("test2", "Test123@", "Test2", "User"),
        ("test3", "Test123@", "Test3", "User"),
        ("test4", "Test123@", "Test4", "User"),
        ("test5", "Test123@", "Test5", "User"),
    ]
    for user in potential_users:
        register(user[0], user[1], user[2], user[3])
    assert accountLimit() == 5
    bad_user = "test6"
    password = "Test123@"
    first = "Test6"
    last = "User"
    assert register(bad_user, password, first, last) != 1
    assert accountLimit() == 5

def test_login(username, password, firstName, lastName):
    register(username, password, firstName, lastName)
    assert login(username, password) == 1
    bad_username = "bad"
    assert login(bad_username, password) != 1

def test_register_existing_user(username, password, firstName, lastName):
    register(username, password, firstName, lastName)
    assert register(username, password, firstName, lastName) != 1

def test_register_bad_password(username, password, firstName, lastName):
    password = "bad"
    assert securePassword(password) != 1

def test_login_existing_user(username, password, firstName, lastName):
    register(username, password, firstName, lastName)
    assert login(username, password) == 1

    # With invalid password
    bad_password = "bad"
    assert verifyCredentials(username, bad_password) != 1

def test_homePage(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWelcome to InCollege!\nPlease choose from one of the options below:\n1. Search for a job\n2. Find someone you know\n3. Learn a new skill\n4. Useful Links\n5. InCollege Important Links\n6. Go to previously visited page\n\n"
    assert out == message

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
    findPage = 2
    route(findPage)
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Find someone you know' feature is still under construction.\n\n"
    assert out == message