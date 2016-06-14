#Initializing the game board
board = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
# Initializing the players
players = [{"name":"noname", "sign":"X"}, {"name":"noname", "sign":"O"}]


def show_board():
	'''
		formats and displays the board with current moves on the board
	'''
	print("-The game board-\n")
	for row in board:
		row_display = ""
		for pos in row:
			row_display +=" " + pos
		print(row_display)
	print("---------------\n")	


def create_players():
	'''
		creates two players and assigns them default signs as a dictionary {players}
	'''
	num = 0
	while num< 2:
		player = input("Please enter the name of player {number}: ".format(number=num+1))
		players[num]["name"] = player
		num += 1
	print("------------------------------------------\n")
	print(" Player {p_name},  your sign is {p_sign}".format(p_name = players[0]["name"], p_sign = players[0]["sign"]))
	print(" Player {p_name},  your sign is {p_sign}".format(p_name = players[1]["name"], p_sign = players[1]["sign"]))


def get_move(sign):
	player_move = str(input("Your move: (Use the number to indicate row and column)"))
	# Because we have coarsed player int input as string we can now use that as string and get both value as col and row
	x = int(player_move[0])-1
	y = int(player_move[1])-1
	if board[x][y] == "-":
		board[x][y] = sign 
	else:
		get_move(sign)
	return (x,y) 


def check_game(arr):
	'''
		this checks if the game is over i.e. if same signs are present in three consecutive rows
		@params the cell of the recently added move as array item [x,y]
		returns ture or false 
	'''
	#getting the position from input array
	x = arr[0]
	y = arr[1]

	#setting default check condition to false
	check = False

	# first let's check if given row meets the condition
	if board[x][0] == board[x][1] and board[x][1] == board[x][2]:
		# Second let's check if given Col meets the condition
		if board[0][y] == board[1][y] and board[1][y] == board[2][y]:
			check = True
		else False
	else False

	if x == y or (x==0 and y==2) or (x==2 and y==0):
		

	

	# Third we have to check the diagonal condition
	return check

def game():
	create_players()
	show_board()
	check = false
	num = 1
	while not check:
		pass






	
		 



