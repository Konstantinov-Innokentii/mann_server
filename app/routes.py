from app import app
from flask import request

import datetime
from flask_sqlalchemy_session import current_session
from app.models import Dinner


@app.route("/dinners", methods=["GET"])
def check_dinner():
    time = datetime.datetime.now().time().replace(second=0, microsecond=0)
    dinners = current_session.query(Dinner).all()
    answer = "0"
    for dinner in dinners:
        dt = time
        if dinner.date == dt:
            answer = str(dinner.size)
            break

    return answer
