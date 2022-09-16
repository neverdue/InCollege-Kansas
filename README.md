# InCollege-Kansas

Hi team, i goofed on pushing and adding a commit message for each individual file.

loginPrompt.py is the "main" function for any login related activites. The function depends on three other imported 
functions which have their own files associated with them.

users.txt stores account usernames and passwords (separated by a single space)

accountCheck.py checks if there are duplicate usernames

accountCount.py checks if there are more than 5 accounts within the users.txt file

passwordCheck.py checks if the passwords fit the criteria of having 1 upper case character, 1 special case character, etc.

-----IMPORTANT NOTE: users.txt needs to have something in it otherwise if the user selects option for existing user, the program will never stop
checking the empty file. The documentation for epic#1 didn't say anything about this technical issue so i left it as is-------
