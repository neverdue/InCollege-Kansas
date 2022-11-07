import pytest
import json
from io import StringIO
from Code.Source.globalVariables import stackInit, dataFileInit, logout
from Code.Source.loginPrompt import signUpPage
from Code.Source.utility import wJson

TESTMODE = True
ACCOUNTFILE = "Code/Data/accounts-test.json"

@pytest.fixture(autouse=True)
def setup():
    dataFileInit(TESTMODE)
    stackInit()

@pytest.mark.parametrize("subscription_inputs, subscription_info, billing_message", 
[("yes\n", "True", "We will start to bill you $10 monthly. Thank you for becoming a PLUS member!"), 
("no\n", "False", "")])
def test_subscriptionOption(capsys, monkeypatch, subscription_inputs, subscription_info, billing_message):
    logout()
    data = json.load(open(ACCOUNTFILE))
    wJson({"accounts": []}, ACCOUNTFILE) # Have to overwrite accounts-test.json else cannot register due to account limit

    # TEST: subscription option is shown with billing message when user registers for new account
    test_inputs = "ctrbl\nPassword123!\nChau\nNguyen\n"
    message = "Would you like to subscribe to become a plus member for $10 a month?\n\t*As a plus member you can send and receive messages from anyone in the InCollege system*\n\t\t\t*rather than only users you are friends with*\n(yes/no):"
    monkeypatch.setattr("sys.stdin", StringIO(test_inputs + subscription_inputs)) 
    signUpPage()
    out, err = capsys.readouterr()
    assert message in out 
    assert billing_message in out 

    # TEST: registered subscription info is stored correctly along with account info
    temp_data = json.load(open(ACCOUNTFILE))
    assert subscription_info == temp_data["accounts"][0]["subscription"]

    wJson(data, ACCOUNTFILE)

