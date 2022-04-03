import flask
from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource

user_service = Blueprint('user_service', __name__, template_folder='templates')
user_service_api = Api(user_service)


class Feed(Resource):
    def get(self):
        return make_response(render_template('base.html'), 200)


class Watch(Resource):
    pass


user_service_api.add_resource(Feed, '/feed')
