import hashlib
from sqlalchemy import Column, Integer, String
from .base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    @classmethod
    def create_password(cls, password, salt):
        return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
    
    def check_password(self, password_from_user, salt):
        return self.password == hashlib.pbkdf2_hmac(
            'sha256', password_from_user.encode('utf-8'), salt, 100000).hex()