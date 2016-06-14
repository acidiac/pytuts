# Amit Chanchal
# Solution to milestone1 assignment Udemy Python Bootcamp
# tictactoe game


# Initializing a empty list for game board as 3*3 matrix
arr = 	[
			["-", "-", "-"],
			["-", "-", "-"],
			["-", "-", "-"]
		]

# function to printout the board
def makeBoard(arr):
	'''
	 Prints out the formatted board
	'''
	for i in arr:
		output = ""
		for j in i:
			output +=j+" "
		print(output)

# funtion to get user move and place add it to the board
def getMove(sign):
	sign  = sign 
	# getting user entry as number as x position and Y position
	pos = int(input("enter pos:"))
	#converting the numbers input to string so that we can split it 
	pos = str(pos)
	# subtracting 1 from the input to account for the first index which is used for labels
	x = int(pos[0]) -1
	y = int(pos[1]) -1
	# check if the place is empty
	if arr[x][y] != "-":
		print("please choose a location that is empty")
		getMove(sign)
	else:
		#adding the sign to the board
		arr[x][y] = sign
		message = "player move registered, "
		return pos


def check(pos):
	'''
		checking if won i,e if consecutive tic or tacs
		returns true for checked
		returns false if not checked
	'''
	print(pos[0])
	print(pos[1])


#testing cases
num = 0
while num < 4:
	makeBoard(arr)
	check(getMove("X"))
	makeBoard(arr)
	num += 1


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









			





