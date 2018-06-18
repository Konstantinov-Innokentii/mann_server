from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api,Resource
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)


from app import routes
from app import models
from app import api_v1
# from app.models import Dinner
# from app.schema import DinnerSchema

# dinner_schema = DinnerSchema()
# dinners_schema = DinnerSchema(many=True)
#
#
# class DinnerResource(Resource):
#
#     def get(self, id):
#         dinner = db.session.query(Dinner)\
#             .get(id)
#         return dinner_schema.dump(dinner).data
#
#     def delete(self, id):
#         dinner = db.session.query(Dinner).get(id)
#         db.session.query(Dinner).filter(Dinner.id == id).delete()
#         db.session.commit()
#         return '', 204
#
#     def put(self, id):
#         assert request.json["id"] == id
#         dinner = dinner_schema.load(request.json, partial=True)
#         db.session.add(dinner.data)
#         db.session.commit()
#         return dinner_schema.dump(dinner.data).data, 201
#
#
# class DinnerListResource(Resource):
#
#     def get(self):
#         dinners = db.session.query(Dinner)
#         return dinners_schema.dump(dinners).data
#
#     def post(self):
#         dinner = dinner_schema.load(request.json).data
#         db.session.add(dinner)
#         db.session.commit()
#         return dinner_schema.dump(dinner).data, 201
#
#
# api.add_resource(DinnerListResource, '/mann/api/v1/dinner')
# api.add_resource(DinnerResource, '/mann/api/v1/dinner/<int:id>')
