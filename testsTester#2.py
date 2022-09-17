import pytest
import passwordCheck
import accountCount
import accountCheck
import loginPrompt

# Initial Screen
# Test case to check if two options are present for Register and Login
# Test case to see that we can access each option

# Register
# Test case to check if output to the screen is for Register
# Test case to check if length > 0 for the username input
# Test case to check if username is in the users.txt file
# Test case to register new username
# Test case to check if password is valid
# Test case to check if 6th account registration attempt, check for error

# Login
# Test case to check if output to the screen is for Login
# Test case to check if length > 0 for the username input
# Test case to check if username is in the users.txt file
    ## Test case to ask for password if user exists
        ### Test case to check if password is valid and print message if valid
    ## Test case to tell them user doesn't exist

def test_validate_password():
    good_password = "GoodPass123@"
    assert passwordCheck.securePassword(good_password) == 1
    bad_passwords = ["pass", "AlmostGoodPasswordButTooLong", "allsmall123@", "HasNoDigit@", "NoSpecChar1"]
    for password in bad_passwords:
        assert passwordCheck.securePassword(password) != 1

def test_account_limit():
    open('users.txt', 'w').close()
    assert accountCount.accountLimit() == 0
    username = "test"
    password = "Test123@"
    loginPrompt.register(username, password)
    assert accountCount.accountLimit() == 1

def test_account_exist():
    open('users.txt', 'w').close()
    username = "test"
    password = "Test123@"
    assert accountCheck.accountExist(username) != 1
    loginPrompt.register(username, password)
    assert accountCheck.accountExist(username) == 1

def test_five_accounts():
    open('users.txt', 'w').close()
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

def test_login():
    open('users.txt', 'w').close()
    username = "test"
    password = "Test123@"
    loginPrompt.register(username, password)
    assert loginPrompt.login(username, password) == 1
    bad_username = "bad"
    assert loginPrompt.login(bad_username, password) != 1

def test_register_existing_user():
    open('users.txt', 'w').close()
    username = "test"
    password = "Test123@"
    loginPrompt.register(username, password)
    assert loginPrompt.register(username, password) != 1

def test_login_existing_user():
    open('users.txt', 'w').close()
    username = "test"
    password = "Test123@"
    loginPrompt.register(username, password)
    assert loginPrompt.login(username, password) == 1

    # With invalid password
    bad_password = "bad"
    assert loginPrompt.verifyCredentials(username, bad_password) != 1