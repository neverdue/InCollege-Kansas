import pytest
import json
import sys
from io import StringIO
from main import main
from potentialConnection import find
from successStory import storyDisplay
from Code.Source.home_page import jobPage, addJobPost, readJobPosts
from Code.Source.globalVariables import userInit

TESTMODE = True
FILENAME = 'jobPosts-test.json'

# Get test user's first & last name and log in
@pytest.fixture(autouse=True)
def setup():
    with open('accounts-test.json', 'r') as json_file:
        data = json.load(json_file)
        test_data = data["accounts"][0]
        pytest.username = test_data["username"]
        pytest.first = test_data["firstName"]
        pytest.last = test_data["lastName"]
    userInit(pytest.username, pytest.first, pytest.last)

# Test: Check if potential connection is an existing user 
def test_find_connection():
    first = pytest.first.lower()
    last = pytest.last.lower()
    assert find(first, last, TESTMODE) == 1

# Test: Nonexisting users with following cases 
@pytest.mark.parametrize("not_users", [("", ""), ("Jennie", "Kim"), ("John", "Greens")])
def test_not_find_connection(not_users):
    bad_first = not_users[0].lower()
    bad_last = not_users[1].lower()
    assert find(bad_first, bad_last, TESTMODE) != 1

# Test: Check if user is greeted by student success story displayed on home screen 
def test_success_story(capfd):
    storyDisplay()
    out, err = capfd.readouterr()
    message = "'Hello, my name is Jane Doe and let me tell you how InCollege has paved a way to success for me.\n"
    message += "Not too long ago, I was freshly graduated student that was having a tough time finding jobs and a direction in life.\n"
    message += "As a freshly graduated student, I didn't have many accomplishments or connections that would help me land job interview,\n"
    message += "but with the tools and connections that InCollege offered, i'm now well off as an independent adult with a strong career path in software engineering.\n"
    message += "Not only am I a software engineer, i'm also now an ex-Navy SEAL, an ex-astronaught, and a part time neurosurgeon!\n"
    message += "All of my accomplishments was stemmed off of me using InCollege. If you too sign up for InCollege, you can also be successful like me!\n"
    message += "Thanks InCollege!'\n\n"
    assert out == message

@pytest.mark.parametrize("test_inputs, messages", 
[(['3', 'Andy', 'Nguyen', '1', 'chau', 'a123!', 'Chau', 'Nguyen'], "Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\n"),
(['3', 'Andy', 'Nguyen', '2', 'user1', 'Password123!'], "Select 1 to sign up for a new InCollege account\nSelect 2 to log in to an existing account\n"),
(['3', 'Jennie', 'Kim'], "They are not yet a part of the InCollege system yet.")])

# Test: If found connection, check if sign-in / sign-up option is prompted 
#       Else, display message 
def test_signPrompt(capsys, monkeypatch, test_inputs, messages) -> None:
    monkeypatch.setattr('builtins.input', lambda _: test_inputs.pop(0))
    main()
    out, err = capsys.readouterr()
    assert messages in out 
    
# Test: Display option to show video about InCollege
def test_play_video(capsys, monkeypatch) -> None:
    test_input = StringIO('4')
    monkeypatch.setattr('sys.stdin', test_input)
    assert main() == None
    out, err = capsys.readouterr()
    assert "Video is now playing" in out 

# Test: Display 'Post a job' option when on 'Find a job' page
def test_find_a_job(capsys, monkeypatch):
    test_input = StringIO('2') # Go to homepage (for testing purpose)
    monkeypatch.setattr('sys.stdin', test_input)
    jobPage()
    out, err = capsys.readouterr()
    assert "Post a job" in out 

# Test: Add 5 jobs
def test_add_job_post(monkeypatch): 
    with open(FILENAME, 'w') as json_file:
        json_file.write('{"numPosts": 0, "jobPosts": []}')

    test_jobs = [["Job1", "Work", "Apple", "Silicon Valley", "$300,000"],
    ["Job2", "Work", "Apple", "Silicon Valley", "$300,000"],
    ["Job3", "Work", "Apple", "Silicon Valley", "$300,000"],
    ["Job4", "Work", "Apple", "Silicon Valley", "$300,000"],
    ["Job5", "Work", "Apple", "Silicon Valley", "$300,000"]]
    for job in test_jobs:
        test_input = '' 
        for value in job:
            test_input += value + '\n'
        monkeypatch.setattr('sys.stdin', StringIO(test_input))
        addJobPost(TESTMODE)

    added_jobs = readJobPosts(TESTMODE)
    for i in range(5):
        assert list(added_jobs[i].values())[0:5] in test_jobs
    
# Test: Maximum 5 posted jobs 
def test_max_num_jobs():
    with open(FILENAME, 'r') as json_file:
        data = json.load(json_file)
        assert data["numPosts"] <= 5

# Test: Warning when try to add more than 5 jobs
def test_exceed_num_jobs(capsys, monkeypatch):
    bad_input = ['a']*5
    monkeypatch.setattr('builtins.input', lambda _: bad_input.pop(0))
    addJobPost(TESTMODE) 
    out, err = capsys.readouterr()
    assert out == "There are already five job posts. Try again later.\n"
