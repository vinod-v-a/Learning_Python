"============ Online Banking System ==============="

class Account:
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.__balance = 0.0

    def deposit(self,amount):

        if isinstance(amount,int) and amount > 0:
            self.__balance+= amount
            print(f"{self.account_holder} deposited {amount} Total __balance: {self.__balance}")
        else:
            print(f"{amount} should be more the zero and Int")
    def withdraw(self,amount):
        if  0 < amount <  self.__balance:
            self.__balance -= amount
            print(f"{self.account_holder} withdraw {amount} ")
        else:
            print("Insufficient funds or invalid amount.")
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.account_holder} account bal: {self.__balance}"





class SavingsAccount(Account):
    def __init__(self,account_holder,interest_rate ):
        super().__init__(account_holder)
        self.interest_rate =interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate
        print(f"Interest for {self.account_holder}'s savings account: ${interest:.2f}")
        return interest


class CheckingAccount(Account):
    def __init__(self,account_holder,overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit
    def withdraw(self,amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            new_balance =self.get_balance() - amount
            self.get_balance(new_balance)
            print(f"{self.account_holder} withdrew ${amount:.2f} (Overdraft allowed)")
        else:
            print("Withdrawal exceeds overdraft limit.")


# === Example Usage ===

# Create a SavingsAccount with 5% interest
# savings = SavingsAccount("Alice", interest_rate=0.05)
# savings.deposit(1000)              # Deposit $1000
# savings.calculate_interest()       # Calculate interest
# print(savings)                     # Print balance

# Create a CheckingAccount with $500 overdraft
# checking = CheckingAccount("Bob", overdraft_limit=500)
# checking.deposit(300)              # Deposit $300
# checking.withdraw(700)            # Withdraw within overdraft limit
# checking.withdraw(200)            # Try to exceed overdraft limit
# print(checking)                   # Print balance








