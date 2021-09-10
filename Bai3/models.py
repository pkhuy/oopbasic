import datetime
import sqlite3
from sqlite3.dbapi2 import PARSE_COLNAMES
import uuid
from dateutil import parser

'''
conn = sqlite3.connect('sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)

c = conn.cursor()

c.execute("""CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    user_id text REFERENCES users (user_id),
    product_id integer REFERENCES products (product_id),
    buy_time timestamp, 
    paid integer
    )""")

c.execute("""CREATE TABLE products (
    product_id interger,
    name text,
    trademark text,
    category text,
    cost integer
    )""")

c.execute("""CREATE TABLE users (
    user_id blob PRIMARY KEY,
    name text,
    phone text
    )""")

c.execute("""CREATE TABLE promotions (
    id integer PRIMARY KEY,
    day timestamp,
    percent real,
    user_id text REFERENCES users (user_id), 
    bought integer
    )""")


conn.commit()

conn.close()
'''

def insert_pro(pro):
    conn = sqlite3.connect('sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO products(product_id, name, trademark, category, cost) VALUES (?, ?, ?, ?, ?)", [
                 pro.id, pro.name, pro.trademark, pro.category, pro.cost])
    conn.commit()
    conn.close()


def insert_user(user):
    conn = sqlite3.connect('sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO users(user_id, name, phone) VALUES (?, ?, ?)", [
            user.id, user.name, user.phone])
    conn.commit()
    conn.close()


def insert_order(order):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO orders(user_id, product_id, buy_time, paid) VALUES (?, ?, ?, ?)", [
            order.user_id, order.pro_id, order.buy_time, order.paid])
    conn.commit()
    conn.close()


def insert_promotion(promotion):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO promotions(day, percent, user_id, bought) VALUES (?, ?, ?, ?)", [
            promotion.day, promotion.percent, promotion.user_id, promotion.bought])
    conn.commit()
    conn.close()


def get_order_of_user(user_id):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT * FROM orders WHERE user_id = '{}'".format(user_id))
    return c.fetchall()


#sap xep mat hang da ban (trong order table) theo filter
def order_by(filter):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT * FROM orders ORDER BY '{}'".format(filter))
    return c.fetchall()


#truy van den cot {value} trong bang {table} co gia tri = {filter}
def get_value_by_filter(table, value, filter):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT * FROM {} WHERE {} = '{}'".format(table, value, filter))
    return c.fetchone()


def select_all(table):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(table))
    return c.fetchall()

#dem 
def check_value_exist(table, value, filter):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT count({}) FROM {} WHERE {} = {}".format(value, table, value, filter))
    return c.fetchall()


#truy van thoi diem mua
def select_buy_time(user_id):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT buy_time, product_id FROM orders, users WHERE orders.user_id = users.user_id AND users.user_id = '{}' ORDER BY orders.buy_time".format(user_id))
    return c.fetchall()


#truy van so lan mua tung ngay trong dot KM
def select_pro_per_day(user_id):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT day, percent, bought FROM promotions, users WHERE promotions.user_id = users.user_id AND users.user_id = '{}'".format(user_id))
    return c.fetchall()


#truy van gia san pham trong order
def select_cost_pro(product_id):
    conn = sqlite3.connect(
        'sale_manager.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    c = conn.cursor()
    c.execute("SELECT products.cost FROM orders, products WHERE products.product_id = orders.product_id AND products.product_id = '{}'".format(product_id))
    return c.fetchone()


#giam gia
def payment(user_id):
    orders = select_buy_time(user_id)
    pro_per_day = select_pro_per_day(user_id)
    sum = 0
    for day in pro_per_day:
        bought = 0
        for order in orders:
            day_count = (order[0] - day[0]).days
            if day_count >= 0 and day_count <= 1:
                cost = select_cost_pro(order[1])
                if cost is None:
                    pass
                elif bought < 5:
                    bought += 1
                    sum += int(cost[0])/2
                else:
                    sum += int(cost[0])

    return sum


