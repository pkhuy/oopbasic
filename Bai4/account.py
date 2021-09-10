import uuid


class Account:
    def __init__(self, name, number, remain):
        self.name = name
        self.number = number
        self.remain = remain

    def withdraw(self, amount):
        self.remain -= amount

    def recharge(self, amount):
        self.remain += amount

    def check_remain(self):
        print(self.remain)

    def send(self, amount, name, number):
        pass


class SavingAccount(Account):
    linked = False
    type = "saving"
    int_rate = 0.6
    
    def __init__(self, name, number, remain):
        super().__init__( name, number, remain)

    def withdraw(self, amount):
        if self.remain < amount:
            print("U don't have enought money")
        else:
            super().withdraw(self, amount)


class CheckingAccount(Account):
    linked = False
    type = "checking"
    def __init__(self, name, number, remain):
        super().__init__(name, number, remain)

    def withdraw(self, amount, accs):
        if self.remain < amount and self.linked:            
            for acc in accs:
                if acc.type == "saving" and acc.number == self.number:
                    if acc.remain + self.remain >= amount:
                        acc.remain -= (amount-self.remain)
                        self.remain = 0
                        break
        else:
            super().withdraw(self, amount)

    


