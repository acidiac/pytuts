#Initializing the game board
board = [["","",""], ["","",""], ["","",""]]
# Initializing the players
players = [{"name":"noname", "sign":"X"}, {"name":"noname", "sign":"O"}]



def show_board():
	'''
		formats and displays the board with current moves on the board
	'''
	for i in board:
		print(i)


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



def get_move(player_index):
	player_move = str(input("Your move %s: (Use the number to indicate row and column)" %(players[player_index]["name"])))
	# Because we have coarsed player int input as string we can now use that as string and get both value as col and row
	x = int(player_move[0])-1
	y = int(player_move[1])-1
	if board[x][y] == "":
		board[x][y] = players[player_index]["sign"] 
	else:
		print("Position already has an entry!")
		get_move(player_index)
	arr = []
	arr.append(x)
	arr.append(y)
	return arr



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
	if board[x][0] == board[x][1] == board[x][2] != "":
		check = True
	elif board[0][y] == board[1][y] == board[2][y] != "":
		check = True
	elif board[0][0] == board[1][1] == board[2][2] !="" or board[0][2]==board[1][1]==board[2][0] !="":
		check = True
	
	return check

	
def board_complete():
	complete = True
	for i in board:
		for j in i:
			if j == "":
				complete = False
	return complete



def game():
	create_players()
	show_board()
	num = 1
	while True or board_complete:
		player_index = num%2
		done = check_game(get_move(player_index))
		if done:
			show_board()
			print(players[player_index]["name"] + " won!!")
			break
		else:
			show_board()
			num += 1




game()

	
		 



