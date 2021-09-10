#Bai 1
class Account:
    remain = 0

    def __init__(self, username, acc_number, remain):
        self.username = username
        self.acc_number = acc_number
        self.remain = remain

    #nap tien
    def deposit(self, amount):
        self.remain += amount

    #rut tien
    def withdraw(self, amount):
        self.remain -= amount


    #phi giao dich
    def tax(self, amount):
        if amount/100 > 1000:
            self.remain -= amount/100
        else:
            self.remain -= 1000
            
    def display(self):
        print(self.__dict__)

#Bai 2
class Win10:
    ver = 10

    def __init__(self, ver):
        self.ver = ver

class Win11(Win10):
    def __init__(self):
        Win10.__init__(self, 11)
