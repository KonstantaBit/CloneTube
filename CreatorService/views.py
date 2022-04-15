import flask
from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
from .forms import addVideoForm
import db_session
from UserService.models import Video

creator_service = Blueprint('creator_service', __name__, template_folder='templates')
creator_service_api = Api(creator_service)


class AddVideo(Resource):
    @login_required
    def get(self):
        form = addVideoForm
        return make_response(render_template('addVideo.html', title='Add video', form=form), 200)

    @login_required
    def post(self):
        form = addVideoForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            video = Video(
                videoName=form.videoName.data(),
                videoDiscription=form.videoDescription.data()
            )
            db_sess.add(video)
            db_sess.commit()
            return redirect('/')
        return make_response(render_template('addVideo.html', title='Add video', form=form), 200)


creator_service_api.add_resource(AddVideo, '/addvideo')
