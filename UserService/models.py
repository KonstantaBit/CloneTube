import datetime
import sqlalchemy
from sqlalchemy import orm
import sqlalchemy.types
from db_session import SqlAlchemyBase
from RegistrationService.models import User


class Video(SqlAlchemyBase):

    __tablename__ = 'videos'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    preview = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    reference = orm.relation("Tag", secondary="association", backref="videos")


association_table = sqlalchemy.Table(
    'association',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('tags', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tags.id')),
    sqlalchemy.Column('videos', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('videos.id'))
)


class Tag(SqlAlchemyBase):

    __tablename__ = 'tags'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    reference = orm.relation("Video", secondary="association", backref="tags")


class Comment(SqlAlchemyBase):

    __tablename__ = 'comments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    user = orm.relation('User')
    video_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("videos.id"))
    video = orm.relation('Video')