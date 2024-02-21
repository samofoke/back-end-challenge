from flask import Blueprint
from app.controllers.user_controller import create_user, login_user

user_blueprint = Blueprint("user_blueprint", __name__)

user_blueprint.route("/user", methods=["POST"])(create_user)
user_blueprint.route("/login", methods=["POST"])(login_user)