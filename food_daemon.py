from app import db
from app.models import Dinner
import threading
import datetime


def get_and_check_dinners():
    threading.Timer(50.0, get_and_check_dinners).start()
    dinners = db.session.query(Dinner).all()
    for dinner in dinners:
        dt = datetime.datetime.now().time().replace(second=0, microsecond=0)
        print(dinner.date)
        print(dt)
        if dinner.date == dt:
            print("ok")
            continue
        else:
            print("nok")

get_and_check_dinners()