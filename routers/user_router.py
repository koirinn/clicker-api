from flask import Blueprint
from controllers import UserController


class UserRouter:
    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller
        self.router = Blueprint("user", __name__)
        self.router.add_url_rule("/signup/", view_func=self.user_controller.signup, methods = ["POST"], endpoint="signup")    
