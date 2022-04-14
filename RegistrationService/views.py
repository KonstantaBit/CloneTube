import flask
from flask import Blueprint, make_response, jsonify, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from .forms import LoginForm, RegisterForm
import db_session
from .models import User
from werkzeug.utils import redirect

reg_service = Blueprint('reg_service', __name__, template_folder='templates')
reg_service_api = Api(reg_service)


class SingUp(Resource):
    def get(self):
        form = RegisterForm()
        return make_response(render_template('signup.html', title='signup', form=form), 200)

    def post(self):
        form = RegisterForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            if db_sess.query(User).filter(User.email == form.email.data).first():
                return render_template('signup.html', title='signup',
                                       form=form,
                                       message="This user is already exist")
            user = User(
                username=form.username.data,
                email=form.email.data
            )
            user.set_password(form.password.data)
            db_sess.add(user)
            db_sess.commit()
            return redirect('/feed')
        return make_response(render_template('signup.html', title='sighup', form=form), 200)


class SingIn(Resource):
    def get(self):
        form = LoginForm()
        return make_response(render_template('signin.html', title='login', form=form), 200)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            db_sess = db_session.create_session()
            user = db_sess.query(User).filter(User.email == form.email.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                return redirect("/")
            return render_template('login.html',
                                   message="Неправильный логин или пароль",
                                   form=form)
        return make_response(render_template('signin.html', title='login', form=form))


reg_service_api.add_resource(SingIn, '/signin')
reg_service_api.add_resource(SingUp, '/signup')
