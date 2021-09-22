"""
Aplicacion creada con flask que permite conectarse a una base de datos y crear notas personales
Para la gestión de la base de datos se utiliza Flask-SQLAlchemy
Para la gestión de usuarios se emplea Flash-login
Se define una función de para borrar y crear las tablas de la base de datos con el commando flask init-db
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import click
from flask.cli import with_appcontext
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Crear las tablas de la base de datos"""

    db.drop_all()
    click.echo("Borrando datos anteriores")
    db.create_all()
    click.echo("Base de datos inicializada")

def init_app(app):
    """Añadir a la aplicación los comandos """

    app.cli.add_command(init_db_command)



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config = True)

    # Cargar el archivo de configuracion de la aplicacion
    app.config.from_pyfile('config.py')

    # Iniciar Plugins
    db.init_app(app)
    login_manager.init_app(app)
    init_app(app)

    with app.app_context():
        from . import routes

        return app

