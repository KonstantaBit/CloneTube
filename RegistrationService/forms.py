from flask_wtf import FlaskForm
from wtforms import EmailField, BooleanField, PasswordField, SubmitField, StringField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Добавить')
