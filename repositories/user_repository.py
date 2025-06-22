from models import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create(self, name: str, password: str, email: str):
        user = User(name = name, password = password, email = email)
        self.db.add(user)
        self.db.commit()
