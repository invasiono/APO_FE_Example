###############################################################################
# Don't add any additional packages; otherwise, you will receive a score of 0 #
##############################################################################
import json

# Question 1: Account class
class Account:
    def __init__(self, account_number: str, owner_name: str, balance: int = 0):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = int(balance)
		

    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = int(value)
    
    def deposit(self, amount: int) -> int:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer")
        self.balance += amount
        print(f"Deposited {amount} VND. New balance: {self.balance} VND.")
        return self.balance
    
    def withdraw(self, amount: int) -> bool:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer")
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds")
            return False

# Question 2: VIPAccount class
class VIPAccount(Account):
    def __init__(self, account_number: str, owner_name: str, balance: int = 0, overdraft_limit: int = 5_000_000):
        super().__init__(account_number, owner_name, balance)
        self._overdraft_limit = int(overdraft_limit)
    
    @property
    def overdraft_limit(self):
        return self._overdraft_limit
    
    @overdraft_limit.setter
    def overdraft_limit(self, value):
        if value < 0:
            raise ValueError("Overdraft limit must be non-negative")
        self._overdraft_limit = int(value)
    
    def withdraw(self, amount: int) -> bool:
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Amount must be a positive integer")
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print(f"Withdraw {amount} VND. New balance: {self.balance} VND")
            return True
        else:
            print("Insufficient funds (overdraft limit reached)")
            return False

# Question 3: Main logic
if __name__ == "__main__":
    # Implement Question 3 logic here (JSON parsing, object creation, calculation, and print result)
    data = '{"account_number": "VIP-WEB-001", "owner_name": "Tran Van B", "balance": 2000000, "limit": 3000000}'
    
    # Parse JSON data
    parsed_data = json.loads(data)
    
    # Create VIPAccount instance
    overdraft_limit = parsed_data.get("limit", 5_000_000)
    account = VIPAccount(
        account_number=parsed_data["account_number"],
        owner_name=parsed_data["owner_name"],
        balance=parsed_data["balance"],
        overdraft_limit=overdraft_limit
    )
    
    # Execute withdrawal transaction
    account.withdraw(4_000_000)
    
    # Print final balance
    print(f"Final Balance: {account.balance} VND.")
