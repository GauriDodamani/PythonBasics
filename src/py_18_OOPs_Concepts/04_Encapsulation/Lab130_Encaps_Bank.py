#Variables are encapsulated by with in the methods and can be access through the calling methods


class Bank:

    def __init__(self,acct_no, balance):    #given 2 args acct_no & balance
        self.__acct = acct_no   #private variable
        self.balance = balance  #public variable


    def check_balance(self):
        print(self.balance)

    def deposit(self,amount):
        self.balance = self.balance + amount


    def check_acct_no(self,is_auth):
        if is_auth == True:
            print(self.__acct)   #
        else:
            print("Invalid")



hdfc = Bank(123456789,50000)   #2 value pass for acct_no & balance
hdfc.check_balance()
hdfc.deposit(1000)
hdfc.check_balance()

hdfc.check_acct_no(True)


