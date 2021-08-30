from flask import Flask, render_template, request
import mariadb

from werkzeug.security import check_password_hash, generate_password_hash

from . import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return "Hola"

    @app.route('/signin',methods=['POST','GET'])
    def signin():
        if request.method == 'POST':
            user = request.form['user']
            password = generate_password_hash(request.form['password'])
            db = db_connect() 
            print(user , password)

        return render_template('signin.html')

    @app.route('/login', methods=['POST','GET'])
    def login():
        if request.method == 'POST':
            user = request.form['user']
            password = generate_password_hash(request.form['password'])
            print(user , password)

        return render_template('login.html')

    return app
