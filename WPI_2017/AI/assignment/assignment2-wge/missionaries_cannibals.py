
import Queue

num_m = 3
num_c = 3

m=1
c=0
left=0
right=1
initalstate=((num_m,num_c),(0,0),left)
Actionspace=[(1,1),(2,0),(1,0),(0,1),(0,2)]
maxdepth=15
def targetok(state):
	rightstate = state[1]
	if rightstate[0] == num_m and rightstate[1] == num_c:
		return True
	else:
		return False

def stateok(state):
	leftstate = state[0]
	rightstate = state[1]
	ship=state[2]

	if ( leftstate[0]>=leftstate[1] or leftstate[0]==0) and (rightstate[0]>=rightstate[1] or rightstate[0]==0):
		return True
	else:
		return False

def tryaction(state,action):
	
	leftstate = state[0]
	rightstate = state[1]
	ship=state[2]
	newstate  = None
	if ship == left:
		if (leftstate[0]<action[0] or leftstate[1]<action[1]):
			return False,None
		else:
			newstate = ((leftstate[0] - action[0],leftstate[1] - action[1]), 
				(rightstate[0] + action[0],rightstate[1] + action[1]), right)
	elif ship == right:
	 	if (rightstate[0]<action[0] or rightstate[1]<action[1]):
			return False,None
		else:
			newstate = ((leftstate[0] + action[0],leftstate[1] + action[1]), 
				(rightstate[0] - action[0],rightstate[1] - action[1]), left)
	if stateok(newstate):
		return True,newstate
	else:
		return False,None	


def gogogo_letus_search(state,depth):
	if depth > maxdepth:
		return False,None
	if targetok(state):
		return True,[]
	res = False
	path = None
	minpathlength=999
	for action in Actionspace:
		isok,newstate = tryaction(state,action)
		if isok:
			subres,subpath = gogogo_letus_search(newstate,depth+1)
			if subres == True:
				res = subres
				if len(subpath + [action])<minpathlength:
					path = subpath + [action]
					minpathlength = len(subpath + [action])

	


	return res ,path
def show(list):
	i = 0
	for val in list:
		mark = "left->right"
		if i % 2 == 0:
			mark = "right->left"
		print "missionaries %d cannibals %d %s"  % (val[0],val[1],mark)
		i+=1
if __name__ == "__main__":
	res,path= gogogo_letus_search(initalstate,0)
	print res
	if res:
		show(path[-1::-1])



