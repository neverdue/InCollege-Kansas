import json

#checks first and last names and prevents duplicate first-last name combinations

def uniqueNames(first, last):
    with open("accounts.json", "r") as json_file:
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

print(uniqueNames("defaut", "default"))