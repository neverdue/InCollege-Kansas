import pytest
import home_page

def test_homePage(capfd):
    home_page.showHomePageGreeting()
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWelcome to InCollege!\nPlease choose from one of the options below:\n1. Search for a job\n2. Find someone you know\n3. Learn a new skill\n\n\n"
    assert out == message

def test_SkillPage(capfd):
    home_page.showSkillPageGreeting()
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nLearn and explore the skill options below!\n1. Communication\n2. Leadership\n3. Collaboration\n4. Responsibility\n5. Time Management\n\nPlease enter a number from 1-5.\nEnter x to return to the home page.\n\n"
    assert out == message

def test_ConstructionMessageJob(capfd):
    home_page.showConstructionMessage("Search for a job")
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Search for a job' feature is still under construction.\n\n"
    assert out == message
    
def test_ConstructionMessageFind(capfd):
    home_page.showConstructionMessage("Find someone you know")
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Find someone you know' feature is still under construction.\n\n"
    assert out == message

def test_ConstructionMessageSkill(capfd):
    home_page.showConstructionMessage("Learn a new skill")
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Learn a new skill' feature is still under construction.\n\n"
    assert out == message

def test_routeJob(capfd):
    jobPage = 1
    home_page.route(jobPage)
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Search for a job' feature is still under construction.\n\n"
    assert out == message

def test_routeFind(capfd):
    findPage = 2
    home_page.route(findPage)
    out, err = capfd.readouterr()
    message = "\n------------------------------------------------------------\n"
    message += "\nWe're sorry!\n'Find someone you know' feature is still under construction.\n\n"
    assert out == message