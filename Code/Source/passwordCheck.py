#Checks for minimum8 characters, maximum of 12 characters, 
#at least one capital letter, one digit, and one special character
def securePassword(password):
    capitalLetter, specialCharCnt, digit = 0, 0, 0

    specialCharacters = ('!','@','#','$', '%','^','&','*','(', ')','-','=','~','[',']',
                        '{','}','|',';',':',"'",',','<','>',".",'?','/')

    #Checks for password length
    if len(password) <= 7:
        print("Password minimum length not met: The password needs to be greater than 7 characters.")
        return
    elif len(password) > 12:
        print("Password maximum length exceeded: The password must be less than 13 characters.")
        return

    #Evaluates characters in the password
    for characters in password:
        for items in specialCharacters:
            if items in characters:
                specialCharCnt+=1
        if characters.isdigit() == 1:
            digit+=1
        elif characters.isupper() == 1:
            capitalLetter+=1

    if capitalLetter <= 0:
        print("Password needs to contain at least 1 capital letter.")
        return
    elif specialCharCnt <= 0:
        print("Password needs to contain at least 1 special character.")
        return
    elif digit <= 0:
        print("Password needs to contain at least 1 digit.")
        return
    return 1