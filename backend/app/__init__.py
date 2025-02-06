from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_dance.contrib.google import make_google_blueprint

db = SQLAlchemy()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    mongo.init_app(app)

    google_bp = make_google_blueprint(client_id="your-google-client-id", client_secret="your-google-client-secret", redirect_to="google_login")
    app.register_blueprint(google_bp, url_prefix="/login")

    with app.app_context():
        from . import routes
        db.create_all()

    return app
