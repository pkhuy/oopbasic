from models import insert_pro, check_value_exist

class Product:
    def __init__(self, id, name, trademark, category, cost):
        self.id = id
        self.name = name
        self.trademark = trademark
        self.category = category
        self.cost = cost


def add_pro():
    pro_id = int(input("Product ID: "))
    while pro_id <= 0 and check_value_exist("products", "product_id", pro_id) > 0:
        print("Product ID must bigger than 0 and unique")
        pro_cost = int(input("Product cost: "))
    pro_name = input("Product name: ")
    pro_trademark = input("Product trademark: ")
    pro_cate = input("Product category: ")
    pro_cost = int(input("Product cost: "))
    while pro_cost <= 0:
        print("Product cost must bigger than 0")
        pro_cost = int(input("Product cost: "))
    new_pro = Product(pro_id, pro_name, pro_trademark, pro_cate, pro_cost)
    insert_pro(new_pro)



#mat hang da ban
def sold():
    #theo ten khach hang
    pass
