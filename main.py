from Code.Source.globalVariables import dataFileInit, stackInit
from Code.Source.mainPage import mainPage


def main():
    dataFileInit()

    #Initialize stack and add login page
    stackInit()
    mainPage()


if __name__ == "__main__":
    main()