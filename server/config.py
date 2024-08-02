from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.comfig["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLACHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)