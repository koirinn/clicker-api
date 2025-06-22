from repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        
    def signup(self, name: str, password: str, email: str):
        self.user_repo.create(name, password, email)