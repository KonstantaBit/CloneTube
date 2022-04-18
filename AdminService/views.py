import flask
from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
import db_session
from AdminService.forms import AddTagForm
from UserService.models import Video, Tag
from decorators import authenticated

admin_service = Blueprint('admin_service', __name__, template_folder='templates')
admin_service_service_api = Api(admin_service)


class AddTag(Resource):
    @authenticated
    def get(self):
        print(current_user)
        if current_user.is_staff == 1:
            form = AddTagForm()
            return make_response(render_template('addtag.html', title='Add tag', form=form), 200)

    @authenticated
    def post(self):
        if current_user.is_staff == 1:
            form = AddTagForm()
            if form.validate_on_submit():
                db_sess = db_session.create_session()
                tag = Tag(
                    content=form.content.data
                )
                db_sess.add(tag)
                db_sess.commit()
                return redirect('/')
            return make_response(render_template('addtag.html', title='Add tag', form=form), 200)


admin_service_service_api.add_resource(AddTag, '/addtag')
