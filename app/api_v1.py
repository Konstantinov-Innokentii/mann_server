from flask_restful import Resource
from flask import request

from app.schema import DinnerSchema
from app.models import Dinner
from app import db
from app import api

dinner_schema = DinnerSchema()
dinners_schema = DinnerSchema(many=True)


class DinnerResource(Resource):

    def get(self, id):
        dinner = db.session.query(Dinner)\
            .get(id)
        return dinner_schema.dump(dinner).data

    def delete(self, id):
        dinner = db.session.query(Dinner).get(id)
        db.session.query(Dinner).filter(Dinner.id == id).delete()
        db.session.commit()
        return '', 204

    def put(self, id):
        assert request.json["id"] == id
        dinner = dinner_schema.load(request.json, partial=True)
        db.session.add(dinner.data)
        db.session.commit()
        return dinner_schema.dump(dinner.data).data, 201


class DinnerListResource(Resource):

    def get(self):
        dinners = db.session.query(Dinner)
        return dinners_schema.dump(dinners).data

    def post(self):
        dinner = dinner_schema.load(request.json).data
        db.session.add(dinner)
        db.session.commit()
        return dinner_schema.dump(dinner).data, 201


api.add_resource(DinnerListResource, '/mann/api/v1/dinner')
api.add_resource(DinnerResource, '/mann/api/v1/dinner/<int:id>')