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
    showConstructionMessage("Search for a job")

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