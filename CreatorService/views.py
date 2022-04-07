import flask
from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource

creator_service = Blueprint('creator_service', __name__, template_folder='templates')
creator_service_api = Api(creator_service)


class AddVideo(Resource):
    def get(self):
        return make_response(render_template('addvideo.html'), 200)


creator_service_api.add_resource(AddVideo, '/addvideo')

