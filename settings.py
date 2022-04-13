from flask import Flask

from UserService.views import user_service
from RegistrationService.views import reg_service
from CreatorService.views import creator_service
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pivo'

# Adding blueprints
app.register_blueprint(user_service)
app.register_blueprint(reg_service)
app.register_blueprint(creator_service)

DEBUG = False