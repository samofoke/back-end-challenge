from app import mongo, bcrypt
from pymongo.errors import PyMongoError
from bson import ObjectId, json_util
from bson.errors import InvalidId
import json

def get_user_by_id(user_id):
    try:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user:
            user_json = json_util.dumps(user)
            return json.loads(user_json), None
    except InvalidId:
        return None, "Invaalid user _id"
    
    return None, "User not found"

def update_user(user_id, update_data):
    try:
        object_id = ObjectId(user_id)
        check_user = mongo.db.users.find_one({"_id": object_id})
        if not check_user:
            return None, "User not found"

        
        if "password" in update_data:
            update_data["password"] = bcrypt.generate_password_hash(update_data["password"]).decode("utf-8")

        mongo.db.users.update_one({"_id": object_id}, {"$set": update_data})
        updated_user = mongo.db.users.find_one({"_id": object_id})
        return updated_user, None

    except InvalidId:
        return None, "Invalid user ID format"
    except PyMongoError as err:
        return None, str(err)
    
def get_all_users():
    users = mongo.db.users.find()
    user_list = []
    for user in users:
        all_users = json.loads(json_util.dumps(users))
        user_list.append(all_users)
    return user_list