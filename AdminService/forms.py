from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class AddTagForm(FlaskForm):
    content = StringField('New tag', validators=[DataRequired()])
    submit = SubmitField('Submit')
