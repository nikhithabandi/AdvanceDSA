class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def credit(self,amount):
        self.__balance+=amount
    def debit(self,amount):
        self.__balance-=amount 
    def display(self):
        print("Current balance:", self.__)
