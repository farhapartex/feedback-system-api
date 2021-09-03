import os
from flask import Flask, render_template
from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import *
from .models import BaseEntity

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db)

# REST API setup
api = Api(app)
parser = reqparse.RequestParser()

