class testClass:
    x =5


def example():
    value = int(input("Enter a value (integer)"))
    stringValue = input("Enter a string")
    return stringValue



    #test_Epic2Tester2 - 9/24/2022
import pytest
from pytest import MonkeyPatch
from Code.Source import globalVariables
from temporary import example, testClass

def test_example(monkeypatch: MonkeyPatch) -> None:
    inputs=[3, "idk"]
    #"lambda _:" - lambda function that does not take in any inputs 
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(testClass, "x", 5)
    #assert testClass.x == 5
    assert example() == "idk"

