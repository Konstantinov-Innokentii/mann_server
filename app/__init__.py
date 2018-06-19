from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)



from app import routes
from app import models
from app import api_v1
from app.db import session

session.init_app(app)
