import mariadb
from flask import g

def db_connect():
    try:
        g.db = mariadb.connect(
            host=app.config['DATABASE_HOST'],
            user=app.config['DTABASE_USER'],
            password=app.config['DATABASE_PASSWORD'],
            database=app.config['DATABASE'],
        )
    except:
        print("No se pudo conectar con la base de datos")

    g.cursor = g.db.cursor()

    return g.d , g.cursor

