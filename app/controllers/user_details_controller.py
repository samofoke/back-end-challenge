from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from bson import json_util
from app.services import details_service
import json

@jwt_required()
def get_user_details(user_id):
    current_user = get_jwt_identity()
    user = details_service.get_user_by_id(current_user)

    check_user_details = details_service.get_user_by_id(user_id)
    if not check_user_details:
        return jsonify({"message": "User not found"}), 404
    

    if user and (user["role"] in ["SUPER", "ADMIN"] or current_user == user_id):
        return jsonify(check_user_details), 200
    else:
        return jsonify({"message": "Unauthorized"}), 403

@jwt_required()   
def update_user_info(user_id):
    current_user = get_jwt_identity()
    user = details_service.get_user_by_id(current_user)

    if user and (user["role"] in ["SUPER", "ADMIN"] or current_user == user_id):
        update_data = request.json
        updated_user, error = details_service.update_user(user_id, update_data)

        if error:
            return jsonify({"message": error}), 400
        if updated_user:
            updated_user_json = json_util.dumps(updated_user)
            return jsonify({"messagge": "User updated successfully", "user": json.loads(updated_user_json)}), 200
        else:
            return jsonify({"message": "Failed to update"}), 500
    else:
        return jsonify({"message": "Unauthorized"}), 403
    
@jwt_required()
def get_all_user_details():
     current_user = get_jwt_identity()
     user = details_service.get_user_by_id(current_user)

     if user and user["role"] == "SUPER":
         all_users = details_service.get_all_users()
         return jsonify(all_users), 200
     else:
         return jsonify({"message": "Unauthorized"}), 403