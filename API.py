
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
    print(students)

def main():
    parseStudentAccountInput()
    return


main()