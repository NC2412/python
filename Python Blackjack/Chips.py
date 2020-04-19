class Chips:

	def __init__(self, total=100):
		self.chips = total
		self.winBet = 0

	def get_value(self):
		return self.chips

	def subtract(self, amount=5):
		self.chips -= amount

	def add(self, amount=0):
		self.chips += amount

	def win_bet(self, amount):
		self.winBet = amount

	def get_win_bet(self):
		return self.winBet