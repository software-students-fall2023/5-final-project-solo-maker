from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

mongo = PyMongo()


def create_app(config_class):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    mongo.init_app(app)

    return app
