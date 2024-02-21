from app.models.user import User
from app import mongo, bcrypt
from datetime import timedelta
from flask_jwt_extended import create_access_token
from pymongo.errors import DuplicateKeyError


def create_user(name, surname, email, password, role):
    existing_user = mongo.db.users.find_one({"email": email})
    if existing_user:
        raise ValueError("A user with this email already exists.")
    
    try:
        new_user = User(name, surname, email, password, role)
        return new_user.save()
    except DuplicateKeyError:
        raise ValueError("This user already exists")
    

def get_user_by_email(email):
    return mongo.db.users.find_one({"email": email})

def verify_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)

def login(email, password):
    user = get_user_by_email(email)
    if user and verify_password(password, user["password"]):
        access_token = create_access_token(identity=str(user["_id"]), expires_delta=timedelta(days=1))
        return access_token
    else:
        raise ValueError("Invalid email and password.")