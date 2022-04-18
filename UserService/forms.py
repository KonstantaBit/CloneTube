from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField, FileField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    content = StringField('', validators=[DataRequired()])
