import random
from string import ascii_letters

class Config:
    SECRET_KEY = ''.join([random.choice(ascii_letters) for _ in range(20)])
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"