class BankAccount():

    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0.0
        
    def withdraw(self, amount):
        if self.balance < amount:
            raise InsuffcientFunds(self.id, amount, self.balance)
        
        self.balance -= amount
        print(str(self.first_name)+str(self.last_name) + " Withdraw " + str(amount))

    def deposit(self, amount):
        self.balance += amount
        print(str(self.first_name)+str(self.last_name) + " Deposited")

    def transfer_from(self, amount, to_account):
        self.withdraw(amount)
        to_account.deposit(amount)
        print(str(self.first_name)+str(self.last_name) + " Transfered " + str(amount) + " to " + to_account.first_name + to_account.last_name)

    def __str__(self):
        return str(self.id) + " " + self.first_name  +  self.last_name + " $ "+ str(self.balance)
        

class InsuffcientFunds(BaseException):

    def __init__(self, id, amount_attempted, current_balance):
        self.id= id
        self.amount_attempted = amount_attempted
        self.current_balance = current_balance
    
    def __str__(self):
        s = "Acct id: " + str(self.id) +  " Attempted: " + str(self.amount_attempted) +  " Current Balance: " + str(self.current_balance) 
        return s

def test_driver():
    bank_account01 = BankAccount(1, "Tom ", "Kip")
    bank_account02 = BankAccount(2, "Bob ", "Ross")
    bank_account03 = BankAccount(3, "Yoda ", "")

    print(bank_account01)
    print(bank_account02)
    print(bank_account03)

    bank_account01.deposit(100.00)
    bank_account02.deposit(100.00)
    bank_account03.deposit(100.00)

    print(bank_account01)
    print(bank_account02)
    print(bank_account03)

    bank_account01.withdraw(53.00)
    print(bank_account01)
    try:
        bank_account02.withdraw(1000.00)
        
    except InsuffcientFunds as e:
        print("Insuffcient Funds")
        print(e)  
    print(bank_account02)

    bank_account01.transfer_from(22.00, bank_account02)
    print(bank_account02)
    print(bank_account01)
    bank_account03.transfer_from(200000.00, bank_account02)
        
    print(bank_account02)
    print(bank_account03)

    print(bank_account01)
    print(bank_account02)
    print(bank_account03)


def main():
    test_driver()
    
main()