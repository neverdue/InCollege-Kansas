import json
from Code.Source.loginPrompt import register
from Code.Source.globalVariables import dataFileInit, stackInit, getDataFile
from Code.Source.homePageOptions import hasProfile

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
                    if(tempList[3] == "plus"):
                        student["subscription"] = True
                    else:
                        student["subscription"] = False
                    student["password"] = tempList[4]
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
    print(students)
    return students

#registers users from Input API data
def runInputAPI():
    for student in parseStudentAccountInput():
        # print(student)
        register(student["username"], student["password"], student["firstname"], student["lastname"], student["subscription"])
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
    #placeholder function for another time
    outputFile = "MyCollege_profiles.txt"
    tupleValue = 1
    f = open(outputFile, "w") 

    with open(getDataFile()) as json_file:
        data = json.load(json_file)
        for user in data["accounts"]:
            if(hasProfile(user["username"])):
                # print(user["username"], "has a profile")
                # print(user["profile"])
                if(user["profile"]["title"]):
                    f.write(user["profile"]["title"] + "\n")
                if(user["profile"]["major"]):
                    f.write(user["profile"]["major"] + "\n")
                if(user["profile"]["university"]):
                    f.write(user["profile"]["university"] + "\n")
                if(user["profile"]["about"]):
                    f.write(user["profile"]["about"] + "\n")
                if(user["profile"]["experience"]):
                    for experience in user["profile"]["experience"]:
                        for entries in experience.items():
                            f.write(entries[tupleValue] + " ")
                        f.write("\n")
                if(user["profile"]["education"]):
                    for education in user["profile"]["education"]:
                        for entries in education.items():
                            f.write(entries[tupleValue] + " ")
                        f.write("\n")
                f.write("=====\n")
    f.close()
    return

#def register(username, password, first, last, subscription):

def main():
    dataFileInit()
    stackInit()
    # runInputAPI()
    # createMyCollege_usersOutput()
    createMyCollege_profilesOutput()
    return


main()