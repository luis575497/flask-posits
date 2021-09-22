"""
Se definen todas las rutas que manejara el servidor para las diferentes peticiones
"""

from flask import Flask, g , url_for ,render_template, request, redirect, flash
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import logout_user, login_required, logout_user, current_user, login_user
from flask import current_app as app
from .schema import db, Posit, User


from . import forms
from . import login_manager


@app.route('/', methods=['GET','POST'])
@login_required
def index():
    """
    Página principal
    GET  request - Construye la página en base a los datos del usuario y el formulario definido para la creación de posits
                   Envía los datos del formulario para crear un nuevo posit a la dirección: /new_posit
    """

    form = forms.posit()

    return render_template('index.html',user=current_user.name,form=form, posits = current_user.posits)

@app.route('/new_posit', methods=['POST'])
@login_required
def new_posit():
    """
    Crear nuevo posit

    POST request - Se crea un posit vinculado al usuario que lo crea
    """

    form = forms.posit()
    if request.method == 'POST' and form.validate_on_submit():
        new_posit = Posit(
                title = form.title.data,
                body = form.body.data,
                category = form.category.data,
                color = form.color.data,
                user = current_user,
                )
        db.session.add(new_posit)
        db.session.commit()
        flash("Nota creada exitosamente","success")
        return redirect(url_for('index'))

    return redirect(url_for('index'))

@app.route('/posit_edit/<id>', methods=['GET','POST'])
@login_required
def posit_edit(id):
    """
    Editar Posit

    GET  request - Se obtiene el id del posit desde la url y con el id se consulta a la base de datos para obtener todos los datos del posit, posteriormente se renderiza la página con el formulario que tiene los datos del posit
    POST request - Se validan los campos del formulario del posit, se establecen los nuevos valores para el posit según el id obtenido de la url
    """

    form = forms.posit()
    posit = Posit.query.get(id)

    if request.method == 'GET':
        form.title.data , form.body.data = posit.title , posit.body
        form.category.process_data(datos.category)
        form.color.process_data(posit.color)
        return render_template('posit_edit.html', form=form)

    if request.method == 'POST' and form.validate_on_submit():
        date = datetime.date.today()
        posit.title = form.title.data
        posit.body = form.body.data
        posit.category = form.category.data
        posit.color = form.color.data
        db.session.commit()
        flash("Nota actualizada exitosamente","success")
        return redirect(url_for('index'))

@app.route('/delete_posit/<id>')
@login_required
def delete_posit(id):
    """
    Se recibe el id del posit enviado mediante la url y se elimina el posit, para finalmente redirigir a la página principal
    """

    posit_id = Posit.query.get(id)
    db.session.delete(posit_id)
    db.session.commit()
    flash("Nota eliminada exitosamente","success")
    return redirect(url_for('index'))

@app.route('/signup',methods=['POST','GET'])
def signup():
    """
    Registro de usuario

    GET request sirve la pagina de registro de usuario
    POST request valida el formulario de registro de usuario
    """

    form = forms.signup_form()

    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user == None:
            password = generate_password_hash(form.password.data)
            user = User(
                    name = form.name.data,
                    password = password,
                    email = form.email.data
                    )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Usuario creado exitosamente","success")
            return redirect(url_for('index'))
        else:
            flash(f"Ya existe un usuario registrado con el correo: {form.email.data}","error")


    return render_template('signup.html', form=form)


@app.route('/login', methods=['POST','GET'])
def login():
    """
    Inicio de sesión de usuario

    GET  request - se verifica que si el usuario ya se encuentra con la sesion activa para dirigirlo a la página principal, de no estar logueado se renderiza la página con el formulario de inicio de sesión
    POST request - se verifica que el formulario tenga los datos correctos, consutla a la base de datos por la existencia de un usuario con el correo electrónico envíado con el usuario y en caso de tener exito se verifica la contraseña. Si la contraseña es correcta se carga al usuario en el LoginManager y se redirige a la página principal
    """

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = forms.log_form()

    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email = email).first()
        if user and check_password_hash(user.password,password):
            login_user(user)
            flash(f"Bienvenido {user.name}","success")
            return redirect(url_for('index'))
        else:
            flash("Usuario o Contraseña no válidos","error")

    return render_template('login.html',form=form)


@app.route("/logout")
@login_required
def logout():
    """Salir de la sesion de usuario."""

    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    """Revisar si el ausuario esta logueado en cada pagina."""

    if user_id is not None:
        return User.query.get(user_id)

    return None

