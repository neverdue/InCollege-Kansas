import pytest
import mock
import builtins
import json
from Code.Source import utility 
from Code.Source import globalVariables
from Code.Source import menuOptions
from Code.Source import loginPrompt
from Code.Source import homePageOptions
from Code.Source.menu import homePage

#--MAKE SURE TO INCLUDE THE SPECIFIC FUNCTION--

# IC-24 Make sure all new pages are functional with the page stack

#pytest test_Epic3.py
#Testing add and removal of general page and subpages of general
#Only option is to go forward 1 page then back to general
def test_general():
    globalVariables.stackInit()

    menuOptions.general()
    assert globalVariables.pageStack == [menuOptions.general]
    #globalVariables.printStack()




#For language localization, when the setting is changed, update the user object in JSON.
def test_language_localization():
    #Check from testing JSON file
    globalVariables.dataFileInit(True)

    #Login to existing user
    loginPrompt.login("user2", "Password123*")

    #Always changes the language of user2 and checks if it does
    file = globalVariables.getDataFile()
    with open(file) as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            if(globalVariables.getUser() == user):
                if globalVariables.getLang() == "English":
                    items["language"] = "Spanish"
                    lang_switch = 1
                elif globalVariables.getLang() == "Spanish":
                    items["language"] = "English"
                    lang_switch = 1

    utility.writeJson(data, file)
    assert lang_switch == 1

# #Update the User object to hold the "GuestControls" features.
# def test_guestControls():




    
