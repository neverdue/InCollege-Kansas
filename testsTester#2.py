import pytest
from Code.Source.passwordCheck import securePassword
from Code.Source.accountCount import accountLimit
from Code.Source.accountCheck import accountExist
from Code.Source.loginPrompt import register, login, verifyCredentials

TESTMODE = True

@pytest.fixture(autouse=True)
def setup():
    open('accounts-test.json', 'w').close()
    with open('accounts-test.json', 'w') as json_file:
        json_file.write('{"accounts": []}')

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
    assert accountLimit(TESTMODE) == 0
    register(username, password, firstName, lastName, TESTMODE)
    assert accountLimit(TESTMODE) == 1

def test_account_exist(username, password, firstName, lastName):
    assert accountExist(username, TESTMODE) != 1
    register(username, password, firstName, lastName, TESTMODE)
    assert accountExist(username, TESTMODE) == 1

def test_five_accounts():
    potential_users = [
        ("test1", "Test123@", "Test1", "User"),
        ("test2", "Test123@", "Test2", "User"),
        ("test3", "Test123@", "Test3", "User"),
        ("test4", "Test123@", "Test4", "User"),
        ("test5", "Test123@", "Test5", "User"),
    ]
    for user in potential_users:
        register(user[0], user[1], user[2], user[3], TESTMODE)
    assert accountLimit(TESTMODE) == 5
    bad_user = "test6"
    password = "Test123@"
    first = "Test6"
    last = "User"
    assert register(bad_user, password, first, last, TESTMODE) != 1
    assert accountLimit(TESTMODE) == 5

def test_login(username, password, firstName, lastName):
    register(username, password, firstName, lastName, TESTMODE)
    assert login(username, password, TESTMODE) == 1
    bad_username = "bad"
    assert login(bad_username, password) != 1

def test_register_existing_user(username, password, firstName, lastName):
    register(username, password, firstName, lastName, TESTMODE)
    assert register(username, password, firstName, lastName, TESTMODE) != 1

def test_register_bad_password(username, password, firstName, lastName):
    password = "bad"
    assert securePassword(password) != 1

def test_login_existing_user(username, password, firstName, lastName):
    register(username, password, firstName, lastName, TESTMODE)
    assert login(username, password, TESTMODE) == 1

    # With invalid password
    bad_password = "bad"
    assert verifyCredentials(username, bad_password) != 1