from abc import ABC, abstractmethod
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self):
        dp = float(input("Enter amount to be deposited: "))
        if dp > 0:
            self.__balance += dp
            print(f"Deposited: {dp}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        wd = float(input("Enter amount to be withdrawn: "))
        if 0 < wd <= self.__balance:
            self.__balance -= wd
            print(f"Withdrawn: {wd}. Remaining balance: {self.__balance}")
        elif wd > self.__balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")
    def check_balance(self):
        print(f"Current balance: {self.__balance}")
account1 = BankAccount(84000)
account1.deposit()
account1.check_balance()
account1.withdraw()
account1.check_balance()