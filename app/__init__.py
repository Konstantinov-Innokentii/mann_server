from flask import Flask
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object('config')
ma = Marshmallow(app)
api = Api(app)

from app import routes
from app import models
from app import api_v1
from app.db import session

session.init_app(app)
