# import pymongo
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    from app_texoit.movies.routes import movies
    from app_texoit.errors.handlers import errors
    app.register_blueprint(errors)
    app.register_blueprint(movies)
    return app
