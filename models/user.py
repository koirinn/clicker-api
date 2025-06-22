from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(100), nullable=False)
    created = Column(DateTime, default=datetime.now)
    