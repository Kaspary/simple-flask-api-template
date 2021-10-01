import datetime
from database import db_session
from user.models import User

def authenticate(username, password):
    user = User.query.filter_by(username=username, is_active=True).first()
    if user and user.check_password(password):
        user.last_login = datetime.datetime.now()
        db_session.commit()
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter_by(id=user_id, is_active=True).first()
