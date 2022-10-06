import json
import time
from Code.Source.globalVariables import addPage, getAdPref, getDataFile, getEmailPref, getSMSPref, getUser, printStack, removePage
from Code.Source.loginPrompt import signUpPage
from Code.Source.utility import printDivider, inputValidation, writeJson

def underConstruction():
    printDivider()
    print("Under construction")
    printDivider()

def blog():
    addPage(blog)
    underConstruction()
    goBackOption()

def careers():
    addPage(careers)
    underConstruction()
    goBackOption()

def developers():
    addPage(developers)
    underConstruction()
    goBackOption()

def browseInCollege():
    addPage(browseInCollege)
    underConstruction()
    goBackOption()

def businessSolutions():
    addPage(businessSolutions)
    underConstruction()
    goBackOption()

def directories():
    addPage(directories)
    underConstruction()
    goBackOption()

def helpCenter():
    addPage(helpCenter)
    printDivider()
    print("We're here to help")
    printDivider()
    goBackOption()

def about():
    addPage(about)
    printDivider()
    print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
    printDivider()
    goBackOption()

def press():
    addPage(press)
    printDivider()
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")
    printDivider()
    goBackOption()

def copyrightNotice():
    addPage(copyrightNotice)
    printStack()
    printDivider()
    print("Copyright Notice 2022 InCollege, Inc. InCollege is a registered trademark of InCollege, Inc. All rights reserved.")
    printDivider()
    goBackOption()

def accessibility():
    addPage(accessibility)
    printDivider()
    print("InCollege makes every effort to ensure that its digital resources are accessible to people with disabilities. As we apply the relevant accessibility standards, we are constantly improving the user experience for everyone.")
    printDivider()
    goBackOption()

def userAgreement():
    addPage(userAgreement)
    printDivider()
    print("InCollege User Agreement: Welcome to InCollege. It is important that you read these terms of use carefully before using our website or mobile application. Using our website or mobile application constitutes your acceptance of these terms and conditions.")
    printDivider()
    goBackOption()

def cookiePolicy():
    addPage(cookiePolicy)
    printDivider()
    print("InCollege's cookie policy states that cookies are used to enhance your visit to our website. You consent to our usage of cookies if you keep using our website to browse.")
    printDivider()
    goBackOption()

def brandPolicy():
    addPage(brandPolicy)
    printDivider()
    print("InCollege Brand Policy: InCollege is a social network for college students. It is a location where students may get to know one another, exchange stories, and discover chances to develop.")
    printDivider()
    goBackOption()
    printDivider()
    goBackOption()

def languages():
    #TODO Need to add languages options
    addPage(languages)
    printDivider()
    print("Languages")
    printDivider()
    goBackOption()

def copyrightPolicy():
    addPage(copyrightPolicy)
    printDivider()
    print("InCollege's copyright policy states that it respects others' intellectual property rights and requests the same courtesy from its users. Our policies are set up to prevent anybody from violating the rights of others, and our material is protected by copyright and trademark laws.")
    printDivider()
    goBackOption()

def goBackOption():
    message = "Select 1 to go back\n"
    print(message)
    inputSelection = inputValidation(1, 2)
    if inputSelection == 1:
        back()

def back():
    lastPage = removePage()
    lastPage()

def general():
    addPage(general)
    printStack()
    message = "You are at the General Page!\n\n"
    message += "Select 1 for Sign Up\nSelect 2 for Help Center\nSelect 3 for About\nSelect 4 for Press\nSelect 5 for Blog\nSelect 6 for Careers\nSelect 7 for Developers\nSelect 8 to go back\n"
    printDivider()
    print(message)
    inputSelection = inputValidation(1, 9)
    
    if inputSelection == 1:
        if signUpPage() == 1:
            return "homePage"
    elif inputSelection == 2:
        helpCenter()
    elif inputSelection == 3:
        about()
    elif inputSelection == 4:
        press()
    elif inputSelection == 5:
        blog()
    elif inputSelection == 6:
        careers()
    elif inputSelection == 7:
        developers()
    elif inputSelection == 8:
        back()

def privacyPolicy():
    addPage(privacyPolicy)
    printDivider()
    message = "Select 1 for Guest Controls\nSelect 2 to go back\n"
    print(message)
    inputSelection = inputValidation(1, 3)
    if inputSelection == 1:
        if guestControls() == -1:
            exit
    elif inputSelection == 2:
        back()

def guestControls():
    addPage(guestControls)
    print("\n\n------Guest Controls------")

    try:
        username = getUser()
        emailPref = getEmailPref()
        SMSPref = getSMSPref()
        adPref = getAdPref()
    except:
        print("Error: No user logged in")
        return -1

    while(True):
        print("\nWould you like to update any of your settings?\n")
        print("Recieve InCollege emails:   ", emailPref)
        print("Recieve SMS from InCollege: ", SMSPref)
        print("Recieve targeted ads:       ", adPref)
        choice = input("\nUpdate emails(1), SMS(2), ads(3), go back to previous page(4): ")

        if choice == '1':
            if emailPref == True:
                print("\nYou will no longer recieve emails from InCollege.\n")
                emailPref = False                
            else:
                print("\nYou will now recieve emails from InCollege.\n")
                emailPref = True
            updateSettings(username, emailPref, SMSPref, adPref)
        elif choice == '2':
            if SMSPref == True:
                print("\nYou will no longer recieve SMS messages from InCollege.\n")
                SMSPref = False
            else:
                print("\nYou will now recieve SMS messages from InCollege.\n")
                SMSPref = True
            updateSettings(username, emailPref, SMSPref, adPref)
        elif choice == '3':
            if adPref == True:
                print("\nYou will no longer recieve targeted ads.\n")
                adPref = False
            else:
                print("\nYou will now recieve targeted ads.\n")
                adPref = True
            updateSettings(username, emailPref, SMSPref, adPref)
        elif choice == '4':
            back()
            return
        else:
            print("Invalid Input. Try again")

        #Allow user to see output
        time.sleep(2)

def updateSettings(username, emailPref, SMSPref, adPref):
    #Update User Settings
    file = getDataFile()
    with open(file) as json_file:
        data = json.load(json_file)
        for items in data["accounts"]:
            user = items["username"]
            if(username == user): 
                items["email"] = "True" if emailPref == True else "False"
                items["SMS"] = "True" if SMSPref == True else "False"
                items["ads"] = "True" if adPref == True else "False"
    writeJson(data, file)