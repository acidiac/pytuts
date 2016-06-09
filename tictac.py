arr = 	[
			["-", "-", "-"],
			["-", "-", "-"],
			["-", "-", "-"]
		]


def makeBoard(arr):
	for i in arr:
		output = ""
		for j in i:
			output +=j+" "
		print(output)

def getMove(player):
	sign = player
	pos = int(input("enter pos:"))
	pos = str(pos)
	x = int(pos[0]) -1
	y = int(pos[1]) -1
	# check if the place is empty
	if arr[x][y] != "-":
		print("please choose a location that is empty")
		getMove(sign)
	else:
		arr[x][y] = sign
		message = "player move registered, "
		return pos


def check():
	'''
		checking if won i,e if consecutive tic or tacs
		returns true for checked
		returns false if not checked
	'''
def game():
	signs = ["X","O"]
	print("player x to play first col are x(1,2,3) and rows are y(1,2,3), as shown below")
	makeBoard()
	num = 0
	test = False 
	while not test:
		'''
		we have to run and alternating turns for both players
		'''
		test = check(getMove(signs[num%2]))
		if test:
			break
			
		num += 1
	print("game over")









			





