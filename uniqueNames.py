import json

# I'm not even sure if this is even needed since since the epic just says: 
# "Assume that all first and last name combinations in the system are unique"

# Returns 1 if all names are unique
# returns 0 if not

def unique():
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
        j = 1
        for names in data["accounts"]:
            fname = names["firstName"]
            lname = names["lastName"]
            fname = fname.lower()
            lname = lname.lower()

            #Check each first and last name with the first and last name of the next account
            for i in range(j, len(data["accounts"])):
                
                nextFname = data["accounts"][i]["firstName"]
                nextLname = data["accounts"][i]["lastName"]
                nextFname = nextFname.lower()
                nextLname = nextLname.lower()

                if fname == nextFname and lname == nextLname:
                    print("First and last names must be unique")
                    return 0
                #Outer loop name checked all names from inner loop. Move on to the next name to check
                if i >= len(data["accounts"])-1:
                    j+=1
                    break
        return 1

unique()