from repositories import UserRepository


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
        
    def signup(self, name: str, password: str, email: str):
        self.user_repo.create(name, password, email)

    def signin(self, email: str, password: str) -> bool:
        user = self.user_repo.get_by_email(email)
        if user is not None and user.password == password:
            return True
        return False