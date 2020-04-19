import Deck

class Hand:

	def __init__(self):
		self.cards = []
		self.total = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)

	def adjust_for_ace(self):
		for index, card in enumerate(self.cards):
			if card.get_rank() == 'Ace' and self.get_total_value() > 21:
				self.cards[index].value = 1

	def get_total_value(self):
		value = 0

		for card in self.cards:
			value = value + card.get_value()

		return value

	def get_card(self, index = 0):
		return self.cards[index]

	def get_cards(self):
		return self.cards

	def reset(self):
		self.cards = []
