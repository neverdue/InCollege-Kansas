# Epic2_Tester#2 files (refer to Rier (tester#2) for questions) - 9/24/2022
import pytest
from pytest import MonkeyPatch
from Code.Source import globalVariables
from Code.Source import home_page

#testing that the creation of the stack as a global, add and removal works properly
def test_pageStack_updates() -> None:
    globalVariables.stackInit()
    globalVariables.addPage("page1")
    globalVariables.addPage("page2")
    globalVariables.addPage("page3")

    #calling this functionality inside another test is an example of what really should be in an isolated test, it shouldn't be here. - Rier
    home_page.findSomeonePage()
    

    assert globalVariables.pageStack == ["page1", "page2", "page3", "findSomeone"]
    #where we should end up
    assert globalVariables.removePage() == "page3"
    #what should be at the back
    assert globalVariables.pageStack[-1] == "page2"

#test to separately see if the empty pageStack() case failed
def test_pageStack_empty() -> None:
    globalVariables.stackInit()
    
    globalVariables.pageStack
    assert globalVariables.removePage() == []

#testing things the findSomeonePage should handle independently
def test_findSomeonePage() -> None:
    globalVariables.stackInit()
    home_page.findSomeonePage()

    assert globalVariables.pageStack == ["findSomeone"]







#@TODO---- implement current user checks

@pytest.mark.skip(reason="Need to refactor before a test is valuable")
def test_currentUserTests():
    assert 1==1 #placeholder

