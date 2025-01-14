from abc import ABC, abstractmethod
import uuid

#Errory pro nereálné částky (thx Chase Bank)
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

#ABS class Account
class Account(ABC):
    def __init__(self, account_number: str):
        self.account_number = account_number
        self.balance = 0.0

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    def get_balance(self) -> float:
        return self.balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value: float):
        self._balance = value

#SavingsAccount
class SavingsAccount(Account):
    def __init__(self, account_number: str, interest_rate: float):
        super().__init__(account_number)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Withdraw amount must be positive.")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds on the savings account.")
        self._balance -= amount

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate

    def __repr__(self):
        return f"ID: {self.account_number} : Balance: {self.balance}"


#CheckingAcc
class CheckingAccount(Account):
    def __init__(self, account_number: str, overdraft_limit: float):
        super().__init__(account_number)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("Withdraw amount must be positive.")
        if self._balance - amount < -self.overdraft_limit:
            raise InsufficientFundsError("Withdrawal exceeds the overdraft limit.")
        self._balance -= amount

    def __repr__(self):
        return f"ID: {self.account_number} : Balance: {self.balance}"


if __name__ == "__main__":
    #Generace random ID acc
    savings = SavingsAccount(str(uuid.uuid4()), 0.03)
    checking = CheckingAccount(str(uuid.uuid4()), 500)

    savings.deposit(1000)
    savings.apply_interest()

    checking.deposit(500)

    try:
        checking.withdraw(1200)
    except InsufficientFundsError as e:
        print(e)

    print(f"Savings Account Balance: {savings.get_balance()}")
    print(f"Checking Account Balance: {checking.get_balance()}")

    print(savings)
    print(checking)