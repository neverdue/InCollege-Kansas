import json

firstName = "John"
lastName = "Doe"

def showHomePageGreeting():
    printDivider()
    print("Welcome to InCollege!")
    print("""Please choose from one of the options below:\n1. Search for a job
2. Find someone you know\n3. Learn a new skill\n\n""")

def showSkillPageGreeting():
    printDivider()
    print("""Learn and explore the skill options below!\n1. Communication\n2. Leadership\n3. Collaboration\n4. Responsibility\n5. Time Management\n
Please enter a number from 1-5.\nEnter x to return to the home page.\n""")

def showConstructionMessage(message):
    printDivider()
    print("We're sorry!\n'{}' feature is still under construction.\n".format(message))

def homePage(): 
    showHomePageGreeting()
    try: 
        user_choice = int(input("Enter your option (1, 2, or 3): "))
    except:
        print("Invalid Input!") 
        return

    while user_choice not in range(1, 4):
        showHomePageGreeting()
        try:
            user_choice = int(input("Enter your option (1, 2, or 3): "))   
        except:
            print("Invalid Input!") 
            return

    route(user_choice)
    returnToHomePage()

def route(user_choice):
    if user_choice == 1:
        jobPage()
    elif user_choice == 2:
        findSomeonePage()
    else:
        showSkillPageGreeting()
        skill_choice = input("Your choice: ")
        while skill_choice != 'x' and skill_choice not in [str(i) for i in range(1, 6)]:
            showSkillPageGreeting()
            skill_choice = input("Your choice: ")
        if skill_choice == 'x':
            homePage()
        else: 
            skillPage(skill_choice)
    
def returnToHomePage():
    user_choice = input('Go back to homepage? (y/n): ')
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Please enter y for yes, n for no: ')
    if user_choice == 'y':
        homePage()
    else: 
        printDivider()
        exit

def jobPage():
    user_choice = input("\n1. Post a job\n2. Home page\n\nEnter your option: ")
    while user_choice != '1' and user_choice != '2':
        user_choice = input('invalid input. \n1. Post a job\n2. Home page\n')
    if user_choice == 2:
        homePage()
    elif user_choice == 1:
        addJobPost()
    
def addJobPost():
    #Checks if already 5 job posts
    with open ('jobPosts.json') as jsonFile:
        data = json.load(jsonFile)
        temp1 = data["numPosts"]
        if temp1 >= 5:
            print("There are already five job posts. Try again later.")
            return

    print("Please input the following information about the job when prompted.\n")
    while True:
        jobTitle = input("Job Title: ")
        length = checkLength(jobTitle, 50)
        if length == True:
            break
    while True:
        jobDescription = input("Job Description: ")
        length = checkLength(jobDescription, 250)
        if length == True:
            break
    while True:
        jobEmployer = input("Employer: ")
        length = checkLength(jobEmployer, 50)
        if length == True:
            break
    while True:
        jobLocation = input("Job Location: ")
        length = checkLength(jobLocation, 50)
        if length == True:
            break
    while True:
        jobSalary = input("Job Salary: ")
        length = checkLength(jobSalary, 50)
        if length == True:
            break
    print("\n")

    jobDictionary = {
        "Title" : jobTitle,
        "Description" : jobDescription,
        "Employer" : jobEmployer,
        "Location" : jobLocation,
        "Salary" : jobSalary,
        "Name" : firstName + ' ' + lastName
    }

    #Appends new post to json file, Increase post count if < 5
    with open ('jobPosts.json') as jsonFile:
        data = json.load(jsonFile)
        temp = data["jobPosts"]
        y = jobDictionary
        temp.append(y)

        #increment number of job posts
        temp1 = data["numPosts"]
        data["numPosts"] = temp1 + 1
    
    writeJson(data, 'jobPosts.json')
        
#Write data to a json File
def writeJson(data, filename):
    with open (filename, "w") as f:
        json.dump(data, f, indent = 4) 

#Read in job posts at application start upclear
def readJobPosts():
    with open('jobPosts.json') as json_file:
        data  = json.load(json_file)
        jobPosts = data["jobPosts"]
    return jobPosts

#Character Limiter Function (Security Measure)
def checkLength(input, limit):
    if len(input) > limit:
        print("\nERROR: Maximum characters of " + str(limit) + " reached.\n")
        return False
    return True

def findSomeonePage():
    showConstructionMessage("Find someone you know")

def skillPage(skill):
    showConstructionMessage("Learn a new skill")

def printDivider():
    print('\n' + '-'*60 + '\n')

def main(): 
    homePage()

if __name__ == "__main__":
    main()