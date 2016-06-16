# Blackjack text based game
# amit chanchal
# version 1

class Player(Object):

	player_moves = []

	player_money = []

	def __init__(self, money):
		self.money = money

	def add_money(self, amount):
		self.money += amount

	def reduce_money(self, amount):
		self.money -= amount

	

class Deck(Object):
	pass


		