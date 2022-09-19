import pytest
from Code.Source.passwordCheck import securePassword
from Code.Source.accountCount import accountLimit
from Code.Source.accountCheck import accountExist
from Code.Source.loginPrompt import register, login, verifyCredentials

TESTMODE = True

@pytest.fixture(autouse=True)
def setup():
    open('users-test.txt', 'w').close()

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

def test_account_limit(username, password):
    assert accountLimit(TESTMODE) == 0
    register(username, password, TESTMODE)
    assert accountLimit(TESTMODE) == 1

def test_account_exist(username, password):
    assert accountExist(username, TESTMODE) != 1
    register(username, password, TESTMODE)
    assert accountExist(username, TESTMODE) == 1

def test_five_accounts():
    potential_users = {
        "test1": "Test123@",
        "test2": "Test123@",
        "test3": "Test123@",
        "test4": "Test123@",
        "test5": "Test123@"
    }
    for username, password in potential_users.items():
        register(username, password, TESTMODE)
    assert accountLimit(TESTMODE) == 5
    bad_user = "test6"
    password = "Test123@"
    assert register(bad_user, password, TESTMODE) != 1
    assert accountLimit(TESTMODE) == 5

def test_login(username, password):
    register(username, password, TESTMODE)
    assert login(username, password, TESTMODE) == 1
    bad_username = "bad"
    assert login(bad_username, password, TESTMODE) != 1

def test_register_existing_user(username, password):
    register(username, password, TESTMODE)
    assert register(username, password, TESTMODE) != 1

def test_register_bad_password(username, password):
    password = "bad"
    assert securePassword(password) != 1

def test_login_existing_user(username, password):
    register(username, password, TESTMODE)
    assert login(username, password, TESTMODE) == 1

    # With invalid password
    bad_password = "bad"
    assert verifyCredentials(username, bad_password, TESTMODE) != 1