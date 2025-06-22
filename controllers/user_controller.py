from services import UserService
from flask import request, jsonify


class UserController:
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    
    def signup(self):
        body = request.get_json()
        name = body.get("name")
        password = body.get("password")
        email = body.get("email")
        self.user_service.signup(name, password, email)
        return jsonify({"message": "пользователь успешно зарегистрирован"}), 201