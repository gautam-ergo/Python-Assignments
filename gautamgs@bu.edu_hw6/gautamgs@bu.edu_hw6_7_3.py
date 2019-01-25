"""
CS 521 Information Structures with Python
#########################################
Module          - HW 6
Creation Date   - 10/28/2018
Student Name    - Gautam Gowrishankar

"""
class Account(object):
    def __init__(self, accountId=0, balance=100, annualInterestRate=0):
        self.__accountId = accountId
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getAccountId(self):
        return self.__accountId

    def setAccountId(self, accountId):
        self.__accountId = accountId

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 1200

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()

    def withdraw(self, withdraw):
        self.__balance -= withdraw

    def deposit(self, deposit):
        self.__balance += deposit


def main():
    acc = Account(1122, 20000, 4.5)
    print("ID - ", acc.getAccountId())
    print("Balance - ", acc.getBalance())
    acc.withdraw(2500)
    print("After Withdrawing 2500 - ", acc.getBalance())
    acc.deposit(3000)
    print("After Depositing 3000 - ", acc.getBalance())
    print("Interest Rate per month -  ", acc.getMonthlyInterestRate())
    print("Interest Per Month - ", acc.getMonthlyInterest())


main()
print("\n -End of Program- ")
