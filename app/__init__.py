import os
from flask import Flask, render_template
from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

db = SQLAlchemy(app)

# REST API setup
api = Api(app)
parser = reqparse.RequestParser()

