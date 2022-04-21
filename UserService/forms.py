from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField, FileField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class CommentForm(FlaskForm):
    content = StringField('', validators=[DataRequired()])


class ProfileEdit(FlaskForm):
    hat_photo = SubmitField('Редактировать')