from Code.Source.globalVariables import dataFileInit, stackInit
from Code.Source.menu import mainPage


def main():
    dataFileInit()

    #Initialize stack and add login page
    stackInit()
    mainPage()


if __name__ == "__main__":
    main()