import flask
from flask import Blueprint, make_response, jsonify, render_template, request
from flask_restful import reqparse, abort, Api, Resource

user_service = Blueprint('user_service', __name__, template_folder='templates')
user_service_api = Api(user_service)


class Feed(Resource):
    def get(self):
        return make_response(render_template('feed.html'), 200)


class Watch(Resource):
    def get(self, video_id):
        return f'Hello {video_id}'


class NoPath(Resource):
    def get(self):
        return flask.redirect('/feed', 200)


user_service_api.add_resource(Feed, '/feed')
user_service_api.add_resource(NoPath, '/')
user_service_api.add_resource(Watch, '/watch/<int:video_id>')
