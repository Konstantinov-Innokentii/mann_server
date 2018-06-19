from marshmallow_sqlalchemy import ModelSchema
from app.models import Dinner

from app.db import session

class DinnerSchema(ModelSchema):
    class Meta:
        sqla_session = session
        model = Dinner


