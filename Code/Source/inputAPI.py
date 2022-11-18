import json
from Code.Source.globalVariables import getJobFile, getStudentAccounts
from Code.Source.utility import getJobsDataBase, parseData_newJobs, writeJson
from Code.Source.loginPrompt import register

def inputMyCollege_jobs(newJobs):
    jobsDataBase = getJobsDataBase()
    jobTitlesDataBase = [job["Title"] for job in jobsDataBase]
    newJobsTitles = [job["Title"] for job in newJobs]
    for title in newJobsTitles:
        if title not in jobTitlesDataBase and len(jobsDataBase) < 10:
            jobsDataBase.append(newJobs[newJobsTitles.index(title)])
    
    with open (getJobFile()) as jsonFile:
        data = json.load(jsonFile)
        data["jobPosts"] = jobsDataBase
        data["numPosts"] = len(jobsDataBase)
    
    writeJson(data, getJobFile())


def parseStudentAccountInput():
    inputFile = getStudentAccounts()
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
def runStudentInputAPI():
    for student in parseStudentAccountInput():
        # print(student)
        register(student["username"], student["password"], student["firstname"], student["lastname"], student["subscription"])
    return

def inputAPIs():
    newJobs = parseData_newJobs()
    inputMyCollege_jobs(newJobs)
    runStudentInputAPI()