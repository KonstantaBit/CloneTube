from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField, SelectField, Form
from wtforms.validators import DataRequired
import sqlite3
import db_session
from UserService.models import Tag



class AddTagForm(FlaskForm):
    content = StringField('Новый тэг', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class DeleteTagForm(FlaskForm):
    tag = SelectField("Тэги для удаления: ", choices='')
