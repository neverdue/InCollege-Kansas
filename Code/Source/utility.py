import json
from Code.Source.globalVariables import getDataFile

#Checks all possible pages to call back to last page visited
def checkPages(page, links):
    if page in links:
        links[page]()
    else:
        print("ERROR. Page not found")

def printDivider():
    print('\n' + '-'*60 + '\n')

#Write data to a json File
def writeJson(data, filename):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4) 

def inputValidation(left, right):
    try:
        inputSelection = int(input("Selection: "))
    except ValueError:
        print("Invalid input!")
        return
    while (inputSelection not in range(left, right)):
        print("Invalid selection, please try again.\n")
        try:
            inputSelection = int(input("Selection: "))
        except ValueError:
            print("Invalid input!")
            exit
    return inputSelection