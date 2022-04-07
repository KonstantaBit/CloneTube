import flask
from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
from .forms import LoginForm

reg_service = Blueprint('reg_service', __name__, template_folder='templates')
reg_service_api = Api(reg_service)


class SingUp(Resource):
    def get(self):
        return make_response(render_template('signup.html'), 200)


class SingIn(Resource):
    def get(self):
        signin_form = LoginForm
        return make_response(render_template('signin.html'), 200)


reg_service_api.add_resource(SingIn, '/signin')
reg_service_api.add_resource(SingUp, '/signup')