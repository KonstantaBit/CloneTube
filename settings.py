from flask import Flask

from UserService.views import user_service
from RegistrationService.views import reg_service
from CreatorService.views import creator_service
from AdminService.views import admin_service
import db_session
from RegistrationService.models import User
from flask_login import LoginManager


app = Flask(__name__, static_folder='./files')
app.config['UPLOAD_FOLDER'] = './files'
app.config['SECRET_KEY'] = 'pivo'
login_manager = LoginManager()
login_manager.init_app(app)



# Adding blueprints
app.register_blueprint(user_service)
app.register_blueprint(reg_service)
app.register_blueprint(creator_service)
app.register_blueprint(admin_service)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

DEBUG = True