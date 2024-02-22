import os
class Config:

    #MONGO String connection
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/dummy")

    # JWT Secret Key
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")