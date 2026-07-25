from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class User(Base):
    __tablename__ = "users" #plural table name bc users table contain many users

    id = Column(Integer, primary_key=True, index=True) #column named id is created in users table
    username = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)