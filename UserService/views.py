import flask
from flask import Blueprint, make_response, jsonify, render_template, request, redirect
from flask_restful import reqparse, abort, Api, Resource
from db_session import create_session
from UserService.models import Video, Comment, Tag
from UserService.forms import CommentForm
from decorators import authenticated
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

user_service = Blueprint('user_service', __name__, template_folder='templates')
user_service_api = Api(user_service)


class Feed(Resource):
    def get(self):
        db_sess = create_session()
        videos = db_sess.query(Video).all()
        tags = db_sess.query(Tag).all()
        return make_response(render_template('feed.html', videos=videos, tags=tags), 200)


class TagFeed(Resource):
    def get(self, tag_id):
        db_sess = create_session()
        tag = db_sess.query(Tag).filter(Tag.id == tag_id).first()
        videos = tag.videos
        return make_response(render_template('tagfeed.html', videos=videos, tag=tag), 200)


class Watch(Resource):
    def get(self, video_id):
        db_sess = create_session()
        form = CommentForm()
        if db_sess.query(Video).filter(Video.id == video_id).first():
            video = db_sess.query(Video).filter(Video.id == video_id).first()
            comments = db_sess.query(Comment).filter(Comment.video_id == video_id).all()
            return make_response(render_template('watch.html', video=video, comments=comments, form=form), 200)
        return 'page not found', 404

    @authenticated
    def post(self, video_id):
        db_sess = create_session()
        form = CommentForm()
        video = db_sess.query(Video).filter(Video.id == video_id).first()
        comments = db_sess.query(Comment).filter(Comment.video_id == video_id).all()
        if form.validate_on_submit():
            video = db_sess.query(Video).filter(Video.id == video_id).first()
            comments = db_sess.query(Comment).filter(Comment.video_id == video_id).all()
            comment = Comment(
                content=form.content.data,
                video_id=video_id,
                user_id=current_user.id
            )
            db_sess.add(comment)
            db_sess.commit()
            return redirect(f'/watch/{video_id}', 301)
        if form_2.validate_on_submit():
            return redirect(f'/edit_video/{video_id}', 301)
        return make_response(
            render_template('watch.html', video=video, comments=comments, form=form, form_2=form_2), 200)


class NoPath(Resource):
    def get(self):
        return flask.redirect('/feed', 301)


user_service_api.add_resource(Feed, '/feed')
user_service_api.add_resource(NoPath, '/')
user_service_api.add_resource(Watch, '/watch/<int:video_id>')
user_service_api.add_resource(TagFeed, '/feed/<int:tag_id>')
