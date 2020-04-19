'''
	BLACKJACK

	Create a blackjack game that is easily playable for the user and implements a capable AI
'''

#importing all necessary modules
import sys, os
from Deck import Deck
from Hand import Hand
from Chips import Chips

#creating variables for the possible card types and values
SUITS = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
RANKS = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
VALUES = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#Instantiating instances of needed classes
D = Deck(SUITS, RANKS)
AI_HAND = Hand()
AI_CHIPS = Chips(50)
USER_HAND = Hand()
USER_CHIPS = Chips(100)

def play_again():
	#ask the user if they would like to play again
		choice = input('Would you like to play another round? (y/n): ')
		if choice == 'n':
			PLAYING = False
		else:
			D.reset()
			AI_HAND.reset()
			USER_HAND.reset()
			PLAYING = True

#win_check decides whether to perform a win or lose bet for the player
def win_check():
	if USER_HAND.get_total_value() > 21:
		bet = USER_CHIPS.get_win_bet()
		AI_CHIPS.add(bet)
		USER_CHIPS.subtract(bet)
		print('Bust! You lose!')

	elif (21 - USER_HAND.get_total_value() < 21 - AI_HAND.get_total_value()):
		bet = USER_CHIPS.get_win_bet()
		AI_CHIPS.subtract(bet)
		USER_CHIPS.add(bet)
		print('You win!')
	else:
		bet = USER_CHIPS.get_win_bet()
		AI_CHIPS.add(bet)
		USER_CHIPS.subtract(bet)
		print('Tie. You lose!')

#next_turn handles the in game input and decisions the computer or user makes
def next_turn():

	choice = ' '

	#players turn
	while choice != 's' and USER_CHIPS.get_value() >= 0 and USER_HAND.get_total_value() < 21:
		choice = input('\nHit or Stand? (h/s): ')

		#hit
		if choice == 'h' and USER_CHIPS.get_value():
			#costs 5 chips
			#add another carsd to deck
			USER_CHIPS.subtract(5)
			USER_HAND.add_card(D.deal())

			#printing users new hand
			print('Your cards are:')
			for card in USER_HAND.get_cards():
				print('\t' + str(card) + ', ' + str(card.get_value()))
			USER_HAND.adjust_for_ace()
			print(USER_HAND.get_total_value())

	#Computer's turn
	if AI_HAND.get_total_value() < 17:
		AI_HAND.add_card(D.deal())
		AI_HAND.adjust_for_ace()

	play_again()

def main():

	PLAYING = True

	while PLAYING:
		#clear the screen
		print('\n'*100)
		#shuffle deck
		D.shuffle()
		#set win bet to a number the user cannot reach
		win_bet = sys.maxsize
		
		#tell user their chip amount and get the win bet
		print('Your current chip amount is: ' + str(USER_CHIPS.get_value()))
		while win_bet > USER_CHIPS.get_value():
			win_bet = int(input('Place your win bet: '))
		USER_CHIPS.win_bet(win_bet)

		#Computer hand
		AI_HAND.add_card(D.deal())
		AI_HAND.add_card(D.deal())
		AI_HAND.adjust_for_ace()

		#User hand
		USER_HAND.add_card(D.deal())
		USER_HAND.add_card(D.deal())
		USER_HAND.adjust_for_ace()
		if USER_HAND.get_total_value() == 21:
			win_check()

		#Printing the computer's hand
		print('\nThe computer\'s hand is:')
		print('\t' + str(AI_HAND.get_card(0)) + '\n')

		#Printing the user's hand adn value
		print('Your cards are:')
		for card in USER_HAND.get_cards():
			print('\t' + str(card) + ', ' + str(card.get_value()))
		print('\tValue: ' + str(USER_HAND.get_total_value()))

		#get the player's and computer's turn
		next_turn()

		#Check if the player or computer won the round
		print(USER_CHIPS.get_win_bet())
		win_check()


#Calling the main function
if __name__ == '__main__':
	main()
