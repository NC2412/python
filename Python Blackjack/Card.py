class Card:

	values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.value = self.values[rank]

	def get_value(self):
		return self.value

	def get_rank(self):
		return self.rank

	def get_suit(self):
		return self.suit

	def __str__(self):
		return self.rank + ' of ' + self.suit

