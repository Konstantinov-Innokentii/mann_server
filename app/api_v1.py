from flask_restful import Resource
from flask import request
from flask_sqlalchemy_session import current_session

from app.schema import DinnerSchema
from app.models import Dinner
from app import api

dinner_schema = DinnerSchema()
dinners_schema = DinnerSchema(many=True)


class DinnerResource(Resource):

    def get(self, id):
        dinner = current_session.query(Dinner)\
            .get(id)
        return dinner_schema.dump(dinner).data

    def delete(self, id):
        dinner = current_session.query(Dinner).get(id)
        current_session.query(Dinner).filter(Dinner.id == id).delete()
        current_session.commit()
        return '', 204

    def put(self, id):
        dinner = dinner_schema.load(request.json, partial=True)
        current_session.add(dinner.data)
        current_session.commit()
        return dinner_schema.dump(dinner.data).data, 201


class DinnerListResource(Resource):

    def get(self):
        dinners = current_session.query(Dinner)
        return dinners_schema.dump(dinners).data

    def post(self):
        print("REQ")
        print(request)
        dinner = dinner_schema.load(request.json).data
        current_session.add(dinner)
        current_session.commit()
        return dinner_schema.dump(dinner).data, 201


api.add_resource(DinnerListResource, '/mann/api/v1/dinner')
api.add_resource(DinnerResource, '/mann/api/v1/dinner/<int:id>')