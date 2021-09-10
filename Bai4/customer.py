from account import Account, SavingAccount, CheckingAccount

class Customer:
    accs = []
    total_acc = len(accs)

    def __init__(self, name):
        self.name = name

    def add_acc(self, new_acc):
        if self.total_acc < 10:
            for acc in self.accs:
                if acc.number == new_acc.number:
                    acc.linked, new_acc.linked = True, True
                    break
            self.accs.append(new_acc)
            self.total_acc += 1


    def take_info(self, number):
        for acc in self.accs:
            if acc.number == number:
                return acc.__dict__
            
    def info_account(self):
        print("Total account: {}\n\n".format(self.total_acc))
        for acc in self.accs:
            if acc.type == "saving":
                print("Account number: {}\nRemain: {}\nInterest rate: {}\n".format(acc.number, acc.remain, acc.int_rate))
            else:
                print("Account number: {}\nRemain: {}\n".format(acc.number, acc.remain))

