# imports
from instapy import InstaPy
from instapy import smart_run


# login credentials for User1
User1 = 'jasminel.ives' 
User1_password = 'no <3'

User2 = input

global chain

chain = [User1]

def findSomeone(User):

	chain.append(User)
	
        #grab mutual followers of User1 --must be public account or your "own" from login credentials
        mutualsList = session.pick_mutual_following(username= User, live_match=True, store_locally=True)
        
        #check each user in mutuals list for two conditions
	for user in mutualsList:
		if user in chain:
			mutualsList.remove(user) #user already in stack

		if user == User2:
			chain.append(User2) #User2 is in mutuals list
			return true
	
        if len(chain) > 10:
		chain.remove(User)
		return false

mutualsList = customSort(mutualsList) #sort mutuals list
	
	for mutual in mutualsList:
		if findSomeone(mutualsList[mutual]) == true:
			return true
	chain.remove(User)
	return false

findSomeone(User1);
