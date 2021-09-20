from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_pyfile('config.py')

    # Iniciar configuracion de base de datos
    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app
