from product import *
import uuid
from promotion import add_promotion
from models import  get_order_of_user, insert_user, get_value_by_filter

def is_uuid(value):
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False

list_customer = []

class Customer:
    def __init__(self, id, name, phone):
        self.id = id
        self.name = name
        self.phone = phone

    def report_order(self):
        for order in get_order_of_user(self.id):
            print(order)

def add_user():
    user_id = uuid.uuid4().hex
    username = input("Username: ")
    phone_number = input("User phone number: ")
    new_user = Customer(user_id, username, phone_number)
    insert_user(new_user)
    add_promotion(user_id)


