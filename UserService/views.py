import flask
from flask import Blueprint, make_response, jsonify, render_template, request
from flask_restful import reqparse, abort, Api, Resource
from db_session import create_session
from UserService.models import Video

user_service = Blueprint('user_service', __name__, template_folder='templates')
user_service_api = Api(user_service)


class Feed(Resource):
    def get(self):
        db_sess = create_session()
        videos = db_sess.query(Video).all()
        return make_response(render_template('feed.html', videos=videos), 200)


class Watch(Resource):
    def get(self, video_id):
        db_sess = create_session()
        if db_sess.query(Video).filter(Video.id == video_id).first():
            video = db_sess.query(Video).filter(Video.id == video_id).first()
            return make_response(render_template('watch.html', video=video), 200)
        return 'page not found', 404


class NoPath(Resource):
    def get(self):
        return flask.redirect('/feed', 301)


user_service_api.add_resource(Feed, '/feed')
user_service_api.add_resource(NoPath, '/')
user_service_api.add_resource(Watch, '/watch/<int:video_id>')
