from Code.Source.globalVariables import dataFileInit, stackInit
from Code.Source.inputAPI import inputAPIs
from Code.Source.mainPage import mainPage
from Code.Source.outputAPI import outputAPIs


def main():
    dataFileInit()
    #Initialize stack and add login page
    stackInit()

    inputAPIs()
    outputAPIs()

    mainPage()


if __name__ == "__main__":
    main()