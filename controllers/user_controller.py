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
    
    def signin(self):
        body = request.get_json()
        password = body.get("password")
        email = body.get("email")
        if self.user_service.signin(email, password):
            return jsonify({"message": "пользователь успешно авторизирован"}), 200
        return jsonify({"message": "такого пользователя нет"}), 400