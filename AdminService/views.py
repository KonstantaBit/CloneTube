import flask
from flask import Blueprint, make_response, jsonify, render_template, request
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect
import db_session
from AdminService.forms import AddTagForm, DeleteTagForm
from UserService.models import Video, Tag
from decorators import authenticated
import sqlite3

admin_service = Blueprint('admin_service', __name__, template_folder='templates')
admin_service_service_api = Api(admin_service)

def func():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    tags = cur.execute("""SELECT content FROM tags""").fetchall()
    con.close()
    ar_with_tags = []
    for i in tags:
        ar_with_tags.append((i[0], i[0]))
    return ar_with_tags


class AddTag(Resource):
    @authenticated
    def get(self):
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
            return make_response(render_template('addtag.html', form=form), 200)


class DeleteTag(Resource):
    @authenticated
    def get(self):
        form = DeleteTagForm()
        form.tag.choices = func()
        if current_user.is_staff == 1:
            db_sess = db_session.create_session()
            tags = db_sess.query(Tag).all()
            return make_response(render_template('deletetag.html', tags=tags, form=form), 200)

    @authenticated
    def post(self):
        form = DeleteTagForm()
        form.tag.choices = func()
        if current_user.is_staff == 1:
            db_sess = db_session.create_session()
            tag = request.form['tag']
            tags = db_sess.query(Tag).filter(Tag.content == tag).first()
            db_sess.delete(tags)
            db_sess.commit()
            return redirect('/')


admin_service_service_api.add_resource(AddTag, '/addtag')
admin_service_service_api.add_resource(DeleteTag, '/deletetag')
