from dotenv import load_dotenv
from os import path, environ

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))


TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'root'
DATABASE_HOST = 'localhost'
DATABASE = 'postit'
