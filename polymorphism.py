class Checking():
	def type(self):
		print('You have a checking account at the Codecademy Bank.')

	def balance(self):
		print('$20 left in your checking.')

class Savings():
	def type(self):
		print('You have a savings account at the Codecademy Bank.')

	def balance(self):
		print('$1000 left in your savings.')

account_a = Checking()
account_b = Savings()

for account in (account_a, account_b):
	account.type()
	account.balance()