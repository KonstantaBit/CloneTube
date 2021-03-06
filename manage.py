import argparse
import os

from settings import *
import db_session
import sqlalchemy

try:
    os.mkdir('./files/media')
except Exception:
    pass
# Здесь будут описаны функции для работы с проектом через командную строку
if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('command', type=str)
    # args = parser.parse_args()
    # if args.command == 'runserver':
    db_session.global_init("db.db")
    app.run(port=8080, host='127.0.0.1', debug=DEBUG)
    # else:
    #     print(f"Unknown command: '{args.command}'\nType 'manage.py -h' for usage.")
