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

class ToDoList:
	def __init__(self, tasks):
		self.tasks = tasks

	def createTask(self, title, description, priority):
		task = Task(title, description, priority)
		self.tasks[title] = task
		print('Task added to the list')

	def completeTask(self, title):
		task = self.tasks[title]
		task.markCompletion()

	def deleteTask(self, title):
		del self.tasks[title]
		print('Task deleted')
	
	def viewTasks(self):
		for key, value in self.tasks.items():
			print(value.display())

	def viewSortedTasksByPriority(self):
		sortedTasks = dict(sorted(self.tasks.items(), key=lambda x: x[1].priority, reverse=True))
		for key, value in sortedTasks.items():
			print(value.display())

	def viewCompletedTasks(self):
		for key, value in self.tasks.items():
			if value.isCompleted():
				print(value.display())

class Task:
	def __init__(self, title, description, priority):
		self.title = title
		self.description = description
		self.priority = priority
		self.completed = False

	def markCompletion(self):
		self.completed = True
		print('Task completed')

	def display(self):
		print('Task')
		print(self.title)
		print(self.description)
		print(self.priority)
		print(self.completed)

	def isCompleted(self):
		return self.completed
	

task1 = Task('Task1', 'Description1', 1)
task2 = Task('Task2', 'Description2', 2)

tasks = {}
tasks[task1.title] = task1
tasks[task2.title] = task2

toDoList = ToDoList(tasks)
toDoList.createTask('Task3', 'Description3', 3)
toDoList.viewTasks()

toDoList.completeTask('Task1')
toDoList.viewCompletedTasks()

toDoList.viewSortedTasksByPriority()
