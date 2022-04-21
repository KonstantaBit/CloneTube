import argparse
from settings import *
import db_session
import os

# Здесь будут описаны функции для работы с проектом через командную строку
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str)
    args = parser.parse_args()
    if args.command == 'runserver':
        db_session.global_init("db.db")
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
    else:
        print(f"Unknown command: '{args.command}'\nType 'manage.py -h' for usage.")
