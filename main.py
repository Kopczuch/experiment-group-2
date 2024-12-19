class AccountManager:
	def __init__(self, accounts):
		self.account = accounts

	def create_account(self, account):
		self.accounts[account.account_number] = account

	def display_accounts_and_balances(self):
		for key, value in self.accounts.items():
			print(key, value.balance)

	def transfer_money(self, amount):
		print("Withdraw from account:")
		wInput = input()
		w = self.accounts[wInput]
		print("Deposit to account:")
		dInput = input()
		d = self.accounts[dInput]

		w.withdraw(amount)
		d.deposit(amount)
		

class BankAccount:
	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance

	def display_balance(self):
		print(self.account_number)
		print("Balance:", self.balance)

	def deposit(self, amount):
		print("Old balance:", self.balance)
		self.balance += amount
		print("New balance:", self.balance)

	def withdraw(self, amount):
		print("Old balance:", self.balance)
		self.balance -= amount
		print("New balance:", self.balance)

