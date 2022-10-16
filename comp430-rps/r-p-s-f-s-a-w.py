import random

# Response: [Items that the response defeats]
game_rules = {
	'Rock': ['pounds out Fire', 'crushes Scissors', 'crushes Sponge'],
	'Paper': ['fans Air', 'covers Rock', 'floats on Water'],
	'Scissors': ['swish through Air', 'cut Paper', 'cut Sponge'],
	'Fire': ['melts Scissors', 'burns Paper', 'burns Sponge'],
	'Sponge': ['soaks Paper', 'uses Air pockets', 'absorbs Water'],
	'Air': ['blows out Fire', 'erodes Rock', 'evaporates Water'],
	'Water': ['erodes Rock', 'puts out Fire', 'rusts Scissors']
}

# asks for user's input of what item they want to play
def user_input():
	user_response = input("Rock, Paper, Scissors, Fire, Sponge, Air, Water? ")
	get_user_response(user_response)

def get_user_response(user_response):
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

def check_tie(user_response, computer_response):
	if user_response == computer_response:
		print('Tie. Try Again.')
		return True
	else:
		return False

def match_to_rules(game_rules, your_item, computer_item):
	# loop through game rules to find your item
	for your_item_key in game_rules.keys():
		# once you find your item
		if your_item == your_item_key:
			# loop through items that your item defeats
			for computer_item_value in game_rules.get(your_item_key):
				# if the computer's item is under the list
				if computer_item in computer_item_value:
					# print out that it defeats computer
					print(your_item, computer_item_value, '. You win.')

	for computer_item_key in game_rules.keys():
		# once you find computer's item
		if computer_item == computer_item_key:
			# loop through items that your computer's item defeats
			for your_item_value in game_rules.get(computer_item_key):
				# if your item is under the list
				if your_item in your_item_value:
					# print out that it defeats you
					print(computer_item, your_item_value, '. I win!')

def play_again():
	play_again = input('Play again? Y/N: ')

	if play_again.title() == 'Y':
		user_input()
	elif play_again.title() == 'N':
		print('Thank you for playing!')
	else:
		print('Invalid. Goodbye.')

def result(user_response):
	print('You entered', user_response)

	computer_response = get_computer_response()

	if check_tie(user_response, computer_response) == False:
		match_to_rules(game_rules, user_response, computer_response)
	else:
		user_input()

	play_again()

def main():
	user_input()

if __name__ == "__main__":
    main()

# Add Pi annunciators
# Comments