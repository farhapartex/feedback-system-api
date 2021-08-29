import os
from flask import Flask, render_template
from flask_restful import Api, reqparse


app = Flask(__name__)

# REST API setup
api = Api(app)
parser = reqparse.RequestParser()

