from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext

db = SQLAlchemy()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Create Database Tables"""
    db.drop_all()
    db.create_all()
    click.echo("Base de datos inicializada")

def init_app(app):
    app.cli.add_command(init_db_command)



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_pyfile('config.py')

    # Iniciar configuracion de base de datos
    db.init_app(app)
    init_app(app)
    with app.app_context():
        from . import routes

        return app



