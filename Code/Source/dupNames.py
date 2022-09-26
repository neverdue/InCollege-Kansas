import json

#checks first and last names and prevents duplicate first-last name combinations
#@TODO - ADD TESTMODE Functionality
def uniqueNames(first, last, TESTMODE = False):
    if TESTMODE==False:
        dataFile = "accounts.json"
    else:
        dataFile = "accounts-test.json"

    with open(dataFile, "r") as json_file:
        data = json.load(json_file)

        first = first.lower()
        last = last.lower()

        for names in data["accounts"]:
            fname = names["firstName"]
            lname = names["lastName"]
            fname = fname.lower()
            lname = lname.lower()

            if first == fname and last == lname:
                print("Error: first and last name must be different than existing user's")
                return 0
    return 1