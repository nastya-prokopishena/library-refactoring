import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")