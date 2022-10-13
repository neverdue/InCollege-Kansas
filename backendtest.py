from Code.Source.globalVariables import dataFileInit, stackInit
from Code.Source.mainPage import mainPage
from Code.Source.utility import createRequest, removeRequest, addToFriendsList, retrieveUser,  getUserFriendList, getUserOutgoingRequestList, getUserIncomingRequestList, getUsersByUniversity, getUsersByMajor, getUsersByLastName

def main():
    dataFileInit()
    # createRequest("testuser1", "testuser2")
    # print("remove user?")
    # test = int(input("press 0 or positive number to remove users"))
    # if test >= 0:
    #     acceptFriendRequest("testuser1","testuser2")
    # #addToFriendsList("testuser1","testuser2")

    # print("outgoingRequestList", getUserOutgoingRequestList("testuser1"))

    # print("incomingRequestList", getUserIncomingRequestList("testuser1"))
    # print("friendslist: ", getUserFriendList("testuser1"))

    
    print(getUsersByUniversity("USF"))
    print(getUsersByLastName("truong"))
    print(getUsersByMajor("computer science"))
    print(getUsersByMajor("computer engineering"))
    
    return

main()