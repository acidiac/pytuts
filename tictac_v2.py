#Initializing the game board
board = [["-","-","-"], ["-","-","-"], ["-","-","-"]]
# Initializing the players
players = {"player1":{"name":"noname", "sign":"X"}, "player2":{"name":"noname", "sign":"O"}}

def show_board():
	print("-The game board-\n")
	for row in board:
		row_display = ""
		for pos in row:
			row_display +=" " + pos
		print(row_display)
	print("---------------\n")	

def create_players():
	num = 1
	while num< 3:
		player = input("Please enter the name of player{number}: ".format(number=num))
		label = "player"+str(num)
		players[label]["name"] = player
		num += 1
	print("------------------------------------------\n")
	print(" Player {p_name},  your sign is {p_sign}".format(p_name = players["player1"]["name"], p_sign = players["player1"]["sign"]))
	print(" Player {p_name},  your sign is {p_sign}".format(p_name = players["player2"]["name"], p_sign = players["player2"]["sign"]))


def get_move(sign):
	player_move = str(input("Your move: (Use the number to indicate row and column)"))
	# Because we have coarsed player int input as string we can now use that as string and get both value as col and row
	x = int(player_move[0])-1
	y = int(player_move[1])-1
	return (x,y) 

print(get_move("x"))