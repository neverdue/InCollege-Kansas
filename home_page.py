def homePage(): 
    printDivider()
    print("Welcome to InCollege!\n")
    message = """Please choose from one of the options below:\n1. Search for a job
2. Find someone you know\n3. Learn a new skill\n\nEnter your option (1, 2, or 3): """

    user_choice = int(input(message))
    while user_choice not in range(1, 4):
        printDivider()
        user_choice = int(input(message))   

    if user_choice == 1:
        jobPage()
    elif user_choice == 2:
        findSomeonePage()
    else:
        printDivider()
        skill_message = """Learn and explore the skill options below!\n1. Communication\n2. Leadership\n3. Collaboration\n4. Responsibility\n5. Time Management\n
Please enter a number from 1-5.\nEnter x to return to the home page.\n
Your choice: """
        skill_choice = input(skill_message)
        while skill_choice != 'x' and skill_choice not in [str(i) for i in range(1, 6)]:
            printDivider()
            skill_choice = input(skill_message)
        if skill_choice == 'x':
            homePage()
        else: 
            skillPage(skill_choice)
    
def jobPage():
    printDivider()
    print("We're sorry!\n'Search for a job' feature is still under construction.\n")
    user_choice = input('Go back to homepage? (y/n): ')
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Please enter y for yes, n for no: ')
    if user_choice == 'y':
        homePage()
    else: 
        printDivider()
        exit

def findSomeonePage():
    printDivider()
    print("We're sorry!\n'Find someone you know' feature is still under construction.\n")
    user_choice = input('Go back to homepage? (y/n): ')
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Please enter y for yes, n for no: ')
    if user_choice == 'y':
        homePage()
    else: 
        printDivider()
        exit

def skillPage(skill):
    printDivider()
    print("We are currently working to provide you with this skill.\n")
    user_choice = input('Go back to homepage? (y/n): ')
    while user_choice != 'y' and user_choice != 'n':
        user_choice = input('Please enter y for yes, n for no: ')
    if user_choice == 'y':
        homePage()
    else: 
        printDivider()
        exit

def printDivider():
    print('\n' + '-'*60 + '\n')

def main(): 
    homePage()

if __name__ == "__main__":
    main()