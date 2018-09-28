from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__) 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://power_user:FCO2018@ec2-35-178-22-37.eu-west-2.compute.amazonaws.com:5432/FCO2018'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models
