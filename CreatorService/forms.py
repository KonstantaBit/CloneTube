from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class addVideoForm(FlaskForm):
    videoName = StringField('Name of your video', validators=[DataRequired()])
    videoDescription = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
