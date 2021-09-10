from models import get_order_of_user, get_value_by_filter, insert_order, select_all, payment
from promotion import END_DAY, START_DAY
#from models import update_cost, add_user, add_pro
from customer import Customer, add_user
from product import Product, add_pro
from order import Order
from models import get_value_by_filter
import datetime

if __name__ == '__main__':
        
    x = 0
    username = ""
    user_id = ""

    #x = 0: go back
    while (x != 6):
        if x == 1:
            add_user()
            x = 0
        elif x == 2:
            add_pro()
            x = 0
        elif x == 3:
            username  = input("What your name?")
            user_id = get_value_by_filter("users", "name", username)
            if user_id is None:
                username = ""
                print("You have not sign up yet")
            x = 0
        elif x == 4:
            while username != "" and x != 0:
                print("choose 0 to exit" )
                for pro in select_all("products"):
                    print(pro)
                select = -1
                while select != 0:
                    select = int(input("Buy something.."))
                    if x != 0:
                        pro_selected = get_value_by_filter("products", "product_id", select)
                        insert_order(Order(user_id[0], select, datetime.datetime.now()))
                x=0
            print("you must login")
            x = 0
        elif x == 5:
            if username == "":
                print("you must login")
                x = 0
            else:
                print("To day is {}. Total amount to paid from {} to {} is: {}".format(
                    datetime.datetime.now(), START_DAY, END_DAY, payment(user_id[0])))
                #print(payment(user_id[0]))
                input("Enter to go back")
                x = 0
        else:
            x = int(input("1. Add user\n 2. Add product\n 3. Login \n 4. Buy \n 5. Invoice \n 6. Exit\n"))
