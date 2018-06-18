from marshmallow_sqlalchemy import ModelSchema
from app.models import Dinner


class DinnerSchema(ModelSchema):
    class Meta:
        model = Dinner


