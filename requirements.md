- Account limit is now 10
- Initialize a friends list for each user (initially empty). This will store their friends' usernames.
- Search option that supports searching by:
  - last name
  - university
  - major
  - Then an option to send friend requests to them. (give each result a number and then ask the user to choose a number for sending a friend request)
- When you login, if you have pending requests, give option to reject or accept. If accept, add each other to each other's friends list.
- Every user gets an option to see their pending requests (the requests they sent to others)
- Add a option to see your network (your friends list) called _"show my network"_

  - this page can be none as well (if they don't have any friends)
  - if they have friends, show their friends' names.
  - Also show an option to disconnect with those friends (remove them from your friends list) (again same strategy enter their option number to disconnect)
  - Disconnecting will remove the each other from each other's friends list.

  Can't send a friend request to yourself
  If user1 sends request to user2 and then if before accepting user2 sends a request to user1 then we just become friends without any pending requests.
  We have three things to be added to the user's object:

  - friends list
  - incoming requests
  - outgoing requests
