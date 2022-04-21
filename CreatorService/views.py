from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.utils import redirect, secure_filename
from .forms import VideoAddForm, VideoEditForm
from db_session import create_session
from UserService.models import Video, Comment, Tag
from RegistrationService.models import User
from decorators import authenticated
import os

creator_service = Blueprint('creator_service', __name__, template_folder='templates')
creator_service_api = Api(creator_service)


class AddVideo(Resource):
    @authenticated
    def get(self):
        form = VideoAddForm()
        return make_response(render_template('addvideo.html', form=form), 200)

    @authenticated
    def post(self):
        form = VideoAddForm()
        if form.validate_on_submit():
            file_preview = form.preview.data
            filename_preview = secure_filename(file_preview.filename)
            os.mkdir(f'./files/media/{form.title.data}')
            file_preview.save(f'./files/media/{form.title.data}/{filename_preview}')
            file_content = form.content.data
            filename_content = secure_filename(file_content.filename)
            file_content.save(f'./files/media/{form.title.data}/{filename_content}')
            db_sess = create_session()
            video = Video(
                title=form.title.data,
                description=form.description.data,
                content=f'media/{form.title.data}/{filename_content}',
                preview=f'media/{form.title.data}/{filename_preview}',
                user_id=current_user.id
            )
            db_sess.add(video)
            db_sess.commit()
            return redirect('/', 301)
        return make_response(render_template('addvideo.html', form=form), 200)


class Channel(Resource):
    def get(self, channel_id):
        db_sess = create_session()
        if db_sess.query(User).filter(User.id == channel_id).first():
            channel = db_sess.query(User).filter(User.id == channel_id).first()
            videos = db_sess.query(Video).filter(Video.user_id == channel_id).all()
            return make_response(render_template('channel.html', user=channel, videos=videos), 200)
        return 'page not found', 404


class Video_del(Resource):
    def get(self, video_id):
        try:
            db_sess = create_session()
            videoi = db_sess.query(Video).filter(Video.id == video_id).first()
            if current_user.is_staff == 1 or current_user.id == videoi.user_id:
                video = db_sess.query(Video).get(video_id)
                os.remove(f'./files/{video.preview}')
                os.remove(f'./files/{video.content}')
                os.rmdir(f"./files/media/{video.title}")
                for i in db_sess.query(Comment).filter(video_id == Comment.video_id).all():
                    db_sess.delete(i)
                db_sess.delete(video)
                videos = db_sess.query(Video).all()
                tags = db_sess.query(Tag).all()
                db_sess.commit()
                return make_response(render_template('feed.html', videos=videos, tags=tags), 302)
            return  'you have no access'
        except Exception:
            return 'you have no access'


class Video_edit(Resource):
    def get(self, video_id):
        try:
            db_sess = create_session()
            videoi = db_sess.query(Video).filter(Video.id == video_id).first()
            if current_user.is_staff == 1 or current_user.id == videoi.user_id:
                form = VideoEditForm()
                db_sess = create_session()
                video = db_sess.query(Video).filter(Video.id == video_id).first()
                form.title.data = video.title
                form.description.data = video.description
                return make_response(render_template('editvideo.html', form=form), 200)
            return 'you have no access'
        except Exception:
            return 'you have no access'

    def post(self, video_id):
        form = VideoEditForm()
        db_sess = create_session()
        video = db_sess.query(Video).filter(Video.id == video_id).first()
        video.title = form.title.data
        video.description = form.description.data
        if form.preview.data:
            os.remove(f'./files/{video.preview}')
            file_preview = form.preview.data
            filename_preview = secure_filename(file_preview.filename)
            file_preview.save(f'./files/media/{video.title}/{filename_preview}')
            video.preview = f'media/{video.title}/{filename_preview}'
        db_sess.commit()
        return redirect('/', 301)


creator_service_api.add_resource(AddVideo, '/addvideo')
creator_service_api.add_resource(Channel, '/channel/<int:channel_id>')
creator_service_api.add_resource(Video_del, '/delete_video/<int:video_id>')
creator_service_api.add_resource(Video_edit, '/edit_video/<int:video_id>')
