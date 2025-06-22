from flask import Flask
from models import Base, engine, get_db
from repositories import UserRepository
from services import *
from controllers import *
from routers import *


app = Flask(__name__)
Base.metadata.create_all(bind=engine)
with get_db() as db:
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_controller = UserController(user_service)
    user_router = UserRouter(user_controller)
    app.register_blueprint(user_router.router, url_prefix = "/users")
    app.run()
    


# @app.route("/")
# def index():
#     return "Hello world"

