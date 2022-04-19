from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField, FileField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class VideoAddForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', widget=TextArea(), validators=[DataRequired()])
    preview = FileField('Превью', validators=[DataRequired()])
    content = FileField('Видео', validators=[DataRequired()])


class VideoEditForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', widget=TextArea(), validators=[DataRequired()])
    preview = FileField('Превью', validators=[DataRequired()])
