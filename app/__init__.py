from flask import Flask
from flask_pymongo import PyMongo;
from pymongo.errors import ConnectionFailure
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from .config import Config


mongo = PyMongo()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)
    bcrypt.init_app(app)

    jwt = JWTManager(app)

    from .blueprints.user_blueprint import user_blueprint
    from .blueprints.details_blueprint import details_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/api/v1")
    app.register_blueprint(details_blueprint, url_prefix="/api/v1")

    #MongoDb connection
    try:
        mongo.db.command('ping')
        print("Connected to MongoDb successfully.")
    except ConnectionFailure:
        print("Failed to connect to MongoDb")

    return app