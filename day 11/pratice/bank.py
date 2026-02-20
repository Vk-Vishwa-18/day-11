class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")

acc1 = BankAccount("Vishwa", 1000)
acc2 = BankAccount("Rahul", 2000)


acc1.deposit(500)
acc1.withdraw(200)
acc1.display_balance()

acc2.deposit(500)
acc2.withdraw(200)
acc2.display_balance()