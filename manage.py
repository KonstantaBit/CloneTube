import argparse
from settings import *
import db_session
import sqlalchemy

# Здесь будут описаны функции для работы с проектом через командную строку
db_session.global_init("db/videos.db")
db_sess = db_session.create_session()
app.run(port=8080, host='127.0.0.1', debug=DEBUG)
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument('command', type=str)
#     args = parser.parse_args()
#     if args.command == 'runserver':
#         db_session.global_init("db.db")
#         app.run(port=8080, host='127.0.0.1', debug=DEBUG)
#     else:
#         print(f"Unknown command: '{args.command}'\nType 'manage.py -h' for usage.")
