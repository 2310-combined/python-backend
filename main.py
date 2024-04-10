from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy

# instantiate Flask functionality
app = Flask(__name__)

# set sqlalchemy URI in application config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # instance of SQL