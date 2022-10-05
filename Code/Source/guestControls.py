from Code.Source.globalVariables import addPage, removePage, getSettingFile, getUser, userInit, getAdPref, getEmailPref, getSMSPref
from Code.Source.home_page import checkPages
import json
import time

def guestControls():
    addPage("guestControls")
    print("\n\n------Guest Controls------")

    #Temp for testing
    #userInit("user1", "first", "last", "english", True, True, True)

    username = getUser()
    emailPref = getEmailPref()
    SMSPref = getSMSPref()
    adPref = getAdPref()

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
        elif choice == '2':
            if SMSPref == True:
                print("\nYou will no longer recieve SMS messages from InCollege.\n")
                SMSPref = False
            else:
                print("\nYou will now recieve SMS messages from InCollege.\n")
                SMSPref = True
        elif choice == '3':
            if adPref == True:
                print("\nYou will no longer recieve targeted ads.\n")
                adPref = False
            else:
                print("\nYou will now recieve targeted ads.\n")
                adPref = True
        elif choice == '4':
            break
        else:
            print("Invalid Input. Try again")

        #Allow user to see output
        time.sleep(2)

    #Update User Settings
    settingFile = getSettingFile()
    with open(settingFile) as json_file:
        data = json.load(json_file)
        for items in data["userSettings"]:
            user = items["username"]
            if(username == user): 
                items["email"] = emailPref
                items["SMS"] = SMSPref
                items["ads"] = adPref


    #Go to previous page
    lastPage = removePage()
    checkPages(lastPage)

#Testing Purposes
#guestControls()