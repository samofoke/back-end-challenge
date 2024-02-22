from app import mongo, bcrypt
from bson import ObjectId


class User:
    def __init__(self, name, surname, email, password, role):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = self.hash_password(password)
        self.role = role

    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")
    
    def save(self):
        user_data = {
           "name": self.name,
           "surname": self.surname,
           "email": self.email,
           "password": self.password,
           "role": self.role
        }
        return mongo.db.users.insert_one(user_data)
    
    @staticmethod
    def find_by_user_id(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)})
    
