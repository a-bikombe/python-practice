"""
ROCK POUNDS OUT FIRE, CRUSHES SCISSORS & SPONGE.
FIRE MELTS SCISSORS, BURNS PAPER & SPONGE.
SCISSORS SWISH THROUGH AIR, CUT PAPER & SPONGE.
SPONGE SOAKS PAPER, USES AIR POCKETS, ABSORBS WATER.
PAPER FANS AIR, COVERS ROCK, FLOATS ON WATER.
AIR BLOWS OUT FIRE, ERODES ROCK, EVAPORATES WATER.
WATER ERODES ROCK, PUTS OUT FIRE, RUSTS SCISSORS.
"""

import random

# Response: [Items that the response defeats]
game_rules = {
	'Rock': ['Fire', 'Scissors', 'Sponge'],
	'Paper': ['Air', 'Rock', 'Water'],
	'Scissors': ['Air', 'Paper', 'Sponge'],
	'Fire': ['Scissors', 'Paper', 'Sponge'],
	'Sponge': ['Paper', 'Air', 'Water'],
	'Air': ['Fire', 'Rock', 'Water'],
	'Water': ['Rock', 'Fire', 'Scissors']
}

# asks for user's input of what item they want to play
def user_input():
	response = input("Rock, Paper, Scissors, Fire, Sponge, Air, Water? ")
	validate_user_response(response)

def validate_user_response(user_response):
	match user_response.title():
		case 'Rock':
			result('Rock')
		case 'Paper':
			result('Paper')
		case 'Scissors':
			result('Scissors')
		case 'Fire':
			result('Fire')
		case 'Sponge':
			result('Sponge')
		case 'Air':
			result('Air')
		case 'Water':
			result('Water')
		case _:
			print('Invalid Response. Please Try Again.')
			user_input()

def get_computer_response():
	# picks a random number from 1 to 7, including 1 and 7, and assigns it to the variable 'rando'. You can use this to select one of the elements for a version where you play the computer.
	computer_number = random.randint(1,7)
	computer_reponse = 'No Response Yet'

	match computer_number:
		case 1:
			computer_reponse = 'Rock'
		case 2:
			computer_reponse = 'Paper'
		case 3:
			computer_reponse = 'Scissors'
		case 4:
			computer_reponse = 'Fire'
		case 5:
			computer_reponse = 'Sponge'
		case 6:
			computer_reponse = 'Air'
		case 7:
			computer_reponse = 'Water'
		case _:
			print('Invalid Computer Response')
	
	print('I entered', computer_reponse)
	return computer_reponse

def match_to_rules(game_rules, your_item, computer_item):
	# loop through game rules to find your item
	for your_item_search in game_rules.keys():
		# once you find your item
		if your_item == your_item_search:
			# loop through items that your item defeats
			for computer_item_search in game_rules.get(your_item_search):
				# if the computer's item is under the list
				if computer_item == computer_item_search:
					# print out that it defeats computer
					print(your_item, 'defeats', computer_item, '. You win.')
				else:
					for computer_item_search in game_rules.keys():
						# once you find computer's item
						if computer_item == computer_item_search:
							# loop through items that your computer's item defeats
							for your_item_search in game_rules.get(computer_item_search):
								# if your item is under the list
								if your_item == your_item_search:
									# print out that it defeats you
									print(computer_item, 'defeats', your_item, '. I win!')
	
	# What happens if you tie? Is there a way to tie?

def result(response_to_analyze):
	print('You entered', response_to_analyze)
	computer_response = get_computer_response()
	match_to_rules(game_rules, response_to_analyze, computer_response)

def main():
	user_input()

if __name__ == "__main__":
    main()

# Clean up
# Add Pi annunciators