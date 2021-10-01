from datetime import datetime
from dataclasses import dataclass
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import validates
from database import BaseModel


@dataclass
class User(BaseModel):

    id: int
    username: str
    date_joined: datetime
    last_login: datetime
    is_active: bool
    is_admin: bool

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True, unique=True, nullable=False)
    password = Column(String(128), unique=True, nullable=False)
    date_joined = Column(DateTime, default=datetime.now(), nullable=False)
    last_login = Column(DateTime, nullable=True)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __str__(self):
        return self.username

    @validates('username')
    def validate_username(self, key, username):
        assert username, 'No username provided'
        assert User.query.filter_by(username=username).first() is None, 'Username is already in use'
        assert len(username)>3 and len(username)<32, 'Username must be between 3 and 32 characters'
        return username

    def set_password(self, password):
        assert password, 'No password provided'
        self.password = generate_password_hash(password)

    def check_password(self, password):
        assert password, 'No password provided'
        return check_password_hash(self.password, password)
