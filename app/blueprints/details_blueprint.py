from flask import Blueprint
from app.controllers.user_details_controller import get_user_details, update_user_info, get_all_user_details

details_blueprint = Blueprint("details_blueprint", __name__)

details_blueprint.route("/user/<string:user_id>", methods=["GET"])(get_user_details)
details_blueprint.route("/user/<string:user_id>", methods=["PUT"])(update_user_info)
details_blueprint.route("/user", methods=["GET"])(get_all_user_details)
