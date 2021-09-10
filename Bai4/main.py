from account import Account, SavingAccount, CheckingAccount
from customer import Customer

def manage_bank():
    pass

if __name__ == '__main__': 
    manage_bank()
    TTB = Customer("Tran Thi B")
    s_acc = SavingAccount("Tran Thi B", 10001221, 20000000)
    c_acc = CheckingAccount("Tran Thi B", 10001221, 3000000)

    TTB.add_acc(s_acc)
    TTB.add_acc(c_acc)

    TTB.info_account()
    c_acc.withdraw(5000000, TTB.accs)
    print(c_acc.__dict__)
    print(s_acc.__dict__)
