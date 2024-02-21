from flask import Flask
from flask_pymongo import PyMongo;
from pymongo.errors import ConnectionFailure
from .config import Congig

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Congig)

    mongo.init_app(app)

    #MongoDb connection
    try:
        mongo.db.command('ping')
        print("Connected to MongoDb successfully.")
    except ConnectionFailure:
        print("Failed to connect to MongoDb")

    return app