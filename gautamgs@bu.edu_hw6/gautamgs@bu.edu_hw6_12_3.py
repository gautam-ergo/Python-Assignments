"""
CS 521 Information Structures with Python
#########################################
Module          - HW 6
Creation Date   - 10/28/2018
Student Name    - Gautam Gowrishankar

"""
class Account:

    def __init__(self, id, balance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def setPreviousPrice(self, previousPrice):
        self.previousPrice = previousPrice

    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def getMonthlyInterest(self):
        return self.__balance * self.getMonthlyInterestRate()


def main():

    accounts = []

    for i in range(0, 10):
        account = Account(i, 100.0)
        accounts.append(account)

    while True:

        id = int(input("\nEnter account id: "))

        while id < 0 or id > 9:
            id = int(input("\nInvalid Id.. Re-enter: "))

        while True:

            print("\n 1 - View Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Exit ")
            selection = int(input("\nEnter your selection: "))

            for acc in accounts:

                if acc.getId() == id:
                    accountObj = acc
                    break

            if selection == 1:
                print(accountObj.getBalance())

            elif selection == 2:
                amt = float(input("\nEnter amount to withdraw: "))
                accountObj.withdraw(amt)
                print("\nUpdated Balance: " + str(accountObj.getBalance()) + " \n")

            elif selection == 3:
                amt = float(input("\nEnter amount to deposit: "))
                accountObj.deposit(amt)
                print("\n Updated Balance: " + str(accountObj.getBalance()) + " \n")

            else:
                return print('Bye')


main()
