# flask-posits
Aplicación web que permite a los usuarios crear notas personales 

En una primera instancia el usuario debe crear una cuenta para poder ingresar al sistema, una vez en el sistema tendrá la capacidad de crear, editar y borrar notas, las notas pueden ser de diferentes colores y categorías.

Se utilizaron los siguiente plugins para Flask
1. Flask-SQLAlchemy
2. Flask-Login
3. WTForms

### Pasos para poder ejecutar la aplicación
1. Cambiar en el archivo instance/config.py la variable `SQLALCHEMY_DATABASE_URI` estableciendo el connector a utilizar, usuario, contraseña, host, puerto y nombre de la base de datos
2. Debe definir una clave secreta (SECRET_KEY) en un archivo .env en el directorio instance/ con la siguiente estructura `SECRET_KEY="misecretkey"`
3. Exportar la variable de entorno FLASK_APP de la siguiente manera `export FLASK_APP=postit`
4. Instalar todos los requisitos para el entorno virtual con pip y el achivo requeriments
5. Ejecutar el comando `flask run`
