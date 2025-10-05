# A simple class that encapsulates banking operation
class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
        
        
    def deposit(self, amount):
        deposit = self.account_balance + amount
        return deposit
    
    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            withdraw = self.account_balance - amount
            return withdraw
        
    def display_balance(self):
        current_balance = f"Current Balance: {self.account_balance}"
        return current_balance
        
