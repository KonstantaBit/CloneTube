from flask import redirect
from flask_login import current_user


def authenticated(func):
    def wrapper(*args, **kwargs):
        try:
            temp = current_user.username
            return func(args, kwargs)
        except AttributeError:
            return redirect("/", 307)
    return wrapper