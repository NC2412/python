import random
import Card

class Deck:

	DECK = []

	def __init__(self, suits, ranks):
		self.deck = []

		for suit in suits:
			for rank in ranks:
				self.deck.append(Card.Card(suit, rank))

		self.DECK = self.deck

	def __str__(self):
		return self.deck

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

	def reset(self):
		self.deck = []
		self.deck = self.DECK