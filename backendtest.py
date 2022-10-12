from Code.Source.globalVariables import dataFileInit, stackInit
from Code.Source.mainPage import mainPage
from Code.Source.utility import createRequest

def main():
    dataFileInit()
    createRequest("testuser1", "testuser2")
    return

main()