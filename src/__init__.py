from flask import Flask
from mongoengine import connect
from config import DBConfig

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    connect(
        db = DBConfig.NAME,
        username = DBConfig.USER,
        password = DBConfig.PASSWORD,
        host     = DBConfig.HOST 
    )

    with app.app_context():
        from .routes import planet_routes
        
        return app