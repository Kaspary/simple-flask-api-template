from datetime import timedelta
from decouple import config

class Config:
    SERVER_NAME = config('SERVER_NAME')
    FLASK_APP = 'wsgi.py'

    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')

    ENV = config('FLASK_ENV')
    DEBUG = config('DEBUG', default=False, cast=bool)
    TESTING = config('TESTING', default=False, cast=bool)

    SECRET_KEY = config('SECRET_KEY')

    JWT_EXPIRATION_DELTA = timedelta(hours=config('JWT_EXPIRATION_DELTA', default=24, cast=int))
