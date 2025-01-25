#banking system using oops

class Account:
    def __init__(self, username, password, balance=0,):

        self.username = username
        self.password = password
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print(f"\nAmount deposited: {amount}\nTotal Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"\nAmount withdrawn: {amount}\nRemaing Balance: {self.balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def get_mini_statement(self):
        print("Mini statement:")
        print(f"Username: {self.username}")
        print(f"Current balance: {self.balance}")

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password):
        if username in self.accounts:
            print("Username already exists")
        else:
            self.accounts[username] = Account(username, password)
            print("\nAccount created successfully")
            print("-------Welcome to PYTHON Bank-------")

    def login(self, username, password):
        if username in self.accounts:
            account = self.accounts[username]
            if account.password == password:
                print("Login Sucess....")
                return account
            else:
                print("Invalid password")
        else:
            print("Invalid username")
        return None

bank = BankingSystem()

while True:
    print("\n")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")
        bank.create_account(username, password)


    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        account = bank.login(username, password)
        if account is not None:
            while True:
                print("\n-----Welcome to PYTHON Bank-----")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check balance")
                print("4. Mini statement")
                print("5. Logout\n")
                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    amount = int(input("Enter amount to deposit: "))
                    account.deposit(amount)

                elif choice == '2':
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdraw(amount)

                elif choice == '3':
                    print(f"Current balance: {account.get_balance()}")

                elif choice == '4':
                    account.get_mini_statement()

                elif choice == '5':
                    print("\n--------THANK YOU VISIT AGAIN--------")
                    break
                else:
                    print("Invalid choice")
    elif choice == '3':
        print("\n------THANK YOU------")
        break

    else:
        print("Invalid choice")
        
