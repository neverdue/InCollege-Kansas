import pytest
import passwordCheck
import accountCount
import accountCheck
import loginPrompt

@pytest.fixture(autouse=True)
def setup():
    open('users.txt', 'w').close()

@pytest.fixture
def username():
    return "test"

@pytest.fixture
def password():
    return "Test123@"

def test_validate_password():
    good_password = "GoodPass123@"
    assert passwordCheck.securePassword(good_password) == 1
    bad_passwords = ["pass", "AlmostGoodPasswordButTooLong", "allsmall123@", "HasNoDigit@", "NoSpecChar1"]
    for password in bad_passwords:
        assert passwordCheck.securePassword(password) != 1

def test_account_limit(username, password):
    assert accountCount.accountLimit() == 0
    loginPrompt.register(username, password)
    assert accountCount.accountLimit() == 1

def test_account_exist(username, password):
    assert accountCheck.accountExist(username) != 1
    loginPrompt.register(username, password)
    assert accountCheck.accountExist(username) == 1

def test_five_accounts():
    potential_users = {
        "test1": "Test123@",
        "test2": "Test123@",
        "test3": "Test123@",
        "test4": "Test123@",
        "test5": "Test123@"
    }
    for username, password in potential_users.items():
        loginPrompt.register(username, password)
    assert accountCount.accountLimit() == 5
    bad_user = "test6"
    password = "Test123@"
    assert loginPrompt.register(bad_user, password) != 1
    assert accountCount.accountLimit() == 5

def test_login(username, password):
    loginPrompt.register(username, password)
    assert loginPrompt.login(username, password) == 1
    bad_username = "bad"
    assert loginPrompt.login(bad_username, password) != 1

def test_register_existing_user(username, password):
    loginPrompt.register(username, password)
    assert loginPrompt.register(username, password) != 1

def test_register_bad_password(username, password):
    password = "bad"
    assert passwordCheck.securePassword(password) != 1

def test_login_existing_user(username, password):
    loginPrompt.register(username, password)
    assert loginPrompt.login(username, password) == 1

    # With invalid password
    bad_password = "bad"
    assert loginPrompt.verifyCredentials(username, bad_password) != 1