import pytest
from Code.Source.home_page import showHomePageGreeting, showSkillPageGreeting, showConstructionMessage, route
from Code.Source.globalVariables import stackInit

def test_homePage(capfd):
    showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWelcome to InCollege!\nPlease choose from one of the options below:\n1. Search for a job\n2. Find someone you know\n3. Learn a new skill\n4. Go to previously visited page\n\n\n"
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