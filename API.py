import json
from Code.Source.loginPrompt import register
from Code.Source.globalVariables import dataFileInit, stackInit, getDataFile

def parseStudentAccountInput():

    inputFile = 'Code/Data/studentAccounts.txt'
    try:
        #indexed list of student accounts to register
        students = []
        #student account object
        student = {}
        temp = []
        tempList = []
        with open(inputFile) as f:
            lines = f.readlines()
            # print("Lines: ", lines)
            for line in lines:
                #Account Separators
                if(line == '=====\n' or line == '====='):
                    student["username"] = tempList[0]
                    student["firstname"] = tempList[1]
                    student["lastname"] = tempList[2]
                    student["password"] = tempList[3]
                    students.append(student)
                    student = {}
                    # print("Students", students)
                    # print(tempList)
                    tempList = []
                    continue
                else:
                    temp = line.split()
                    # print("Line split", temp)
                    for i in temp:
                        # print(i)
                        tempList.append(i)
            # print(students)
    except:
        print("No API Input: studentsAccounts.txt was not found")

    # print("List of students to be added: ",students)
    # print(students)
    return students

#registers users from Input API data
def runInputAPI():
    for student in parseStudentAccountInput():
        # print(student)
        register(student["username"], student["password"], student["firstname"], student["lastname"], False)
    return

def createMyCollege_usersOutput():
    print()
    #placeholder function for another time
    outputFile = "MyCollege_user.txt"

    f = open(outputFile, "w") 

    with open(getDataFile()) as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            subscription = ""
            if(user["subscription"] == "False"):
                subscription = "standard"
            else:
                subscription = "plus"
            
            f.write(user["username"] + ' ' + subscription + "\n")
            f.write("=====\n")

    f.close()
    return

def createMyCollege_profilesOutput():
    print()
    #placeholder function for another time
    outputFile = "MyCollege_profiles.txt"

    f = open(outputFile, "w") 

    with open(getDataFile()) as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            #need some way to check if they have profile, and stuff like that.
            # if ":
            #     f.write("=====\n")
            print()
    f.close()
    return

#def register(username, password, first, last, subscription):

def main():
    dataFileInit()
    stackInit()
    # runInputAPI()
    createMyCollege_usersOutput()
    return


main()