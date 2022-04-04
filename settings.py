from flask import Flask

from UserService.views import user_service
from RegistrationService.views import reg_service

app = Flask(__name__)
app.register_blueprint(user_service)
app.register_blueprint(reg_service)

DEBUG = False