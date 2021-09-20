from dotenv import load_dotenv
from os import path, environ

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir,'.env'))


TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = "postgresql://posit:posit@localhost:5432/posit"
SQLALCHEMY_TRACK_MODIFICATIOS = False

