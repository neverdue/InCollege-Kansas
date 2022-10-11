# InCollege-Kansas

Folder structure:

```
table of contents
├── README.md
├── users.txt (list of users)
├── users-test.txt (list of users for testing)
├── main.py (main script)
├── tests.py (test script for InCollege features)
├── testsTester#2.py (test script for login/registration features)
├── Code
│   ├── Source - All functionality files
```

loginPrompt.py is the "main" function for any login related activites. The function depends on three other imported
functions which have their own files associated with them.

users.txt stores account usernames and passwords (separated by a single space)

users-test.txt stores account usernames and passwords (separated by a single space) for testing purposes

accountCheck.py checks if there are duplicate usernames

accountCount.py checks if there are more than 10 accounts within the users.txt file

passwordCheck.py checks if the passwords fit the criteria of having 1 upper case character, 1 special case character, etc.
