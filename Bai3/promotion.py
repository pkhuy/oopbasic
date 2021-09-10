from models import insert_promotion, payment
import datetime


START_DAY = datetime.datetime(2021, 9, 7)
END_DAY = datetime.datetime(2021, 9, 10)
DAY_COUNT = (END_DAY - START_DAY).days
PERCENT = 0.5


class Promotion:
    max_buy = 5
    def __init__(self, day, user_id, percent):
        self.day = day
        self.percent = percent
        self.user_id = user_id
        self.bought = 0


def add_promotion(user_id):
    for single_day in (START_DAY + datetime.timedelta(n) for n in range(DAY_COUNT)):
        insert_promotion(Promotion(single_day, user_id, PERCENT))
