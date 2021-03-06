from flask import Blueprint, make_response, render_template, redirect
from flask_login import login_user, logout_user
from flask_restful import Api, Resource

from db_session import create_session
from .forms import LoginForm, RegisterForm
from .models import User

reg_service = Blueprint('reg_service', __name__, template_folder='templates')
reg_service_api = Api(reg_service)


class SignUp(Resource):
    def get(self):
        form = RegisterForm()
        return make_response(render_template('signup.html', title='signup', form=form), 200)

    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            db_sess = create_session()
            if db_sess.query(User).filter(User.username == form.username.data).first():
                return make_response(render_template('signup.html', form=form, message="Этот логин уже существует"),
                                     200)
            user = User(
                username=form.username.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            login_user(user, remember=form.remember_me.data)
            return redirect("/", 301)
        return make_response(render_template('signup.html', form=form), 200)


class SignIn(Resource):
    def get(self):
        form = LoginForm()
        return make_response(render_template('signin.html', form=form), 200)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            db_sess = create_session()
            user = db_sess.query(User).filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/", 301)
            return make_response(render_template('signin.html', message="Неправильный логин или пароль", form=form))
        return make_response(render_template('signin.html', form=form))


class SignOut(Resource):
    def get(self):
        logout_user()
        return redirect("/", 301)


reg_service_api.add_resource(SignIn, '/signin')
reg_service_api.add_resource(SignUp, '/signup')
reg_service_api.add_resource(SignOut, '/signout')
