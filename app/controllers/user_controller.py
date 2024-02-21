from flask import request, jsonify
from app.services import user_service

def create_user():
    data = request.json
    try:
        user = user_service.create_user(data["name"], data["surname"], data["email"], data["password"], data["role"])
        return jsonify({"message": "User created Successfully", "user_id": str(user.inserted_id)}), 201
    except ValueError as err:
        return jsonify({"error": str(err)}), 400
    

def login_user():
    try:
        email = request.json.get("email")
        password = request.json.get("password")
        access_token = user_service.login(email, password)
        return jsonify({"access_token": access_token}), 200
    except ValueError as err:
        return jsonify({"error": str(err)}), 401