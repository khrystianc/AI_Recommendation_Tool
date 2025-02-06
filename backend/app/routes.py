from flask import request, jsonify, redirect, url_for
from flask_restful import Api, Resource
from flask_dance.contrib.google import google
from . import db, mongo
from .models import User, Item, UserPreference
from .recommendation import generate_recommendations

api = Api()

class GoogleLogin(Resource):
    def get(self):
        if not google.authorized:
            return redirect(url_for("google.login"))
        resp = google.get("/plus/v1/people/me")
        assert resp.ok, resp.text
        email = resp.json()["emails"][0]["value"]
        user = User.query.filter_by(email=email).first()
        if not user:
            user = User(email=email)
            db.session.add(user)
            db.session.commit()
        return jsonify({"message": "Logged in as {}".format(email)})

class ItemList(Resource):
    def get(self):
        items = Item.query.all()
        return jsonify([item.to_dict() for item in items])

    def post(self):
        data = request.get_json()
        item = Item(title=data['title'], description=data['description'], metadata=data['metadata'])
        db.session.add(item)
        db.session.commit()
        return jsonify(item.to_dict())

class Recommendation(Resource):
    def get(self, user_id):
        user_preferences = UserPreference.query.filter_by(user_id=user_id).all()
        recommendations = generate_recommendations(user_preferences)
        return jsonify(recommendations)

api.add_resource(GoogleLogin, '/login/google')
api.add_resource(ItemList, '/items')
api.add_resource(Recommendation, '/recommendations/<int:user_id>')

def init_app(app):
    api.init_app(app)
