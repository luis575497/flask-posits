from flask import Flask, g , url_for ,render_template, request, redirect, flash
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager
from flask import current_app as app
from .schema import db, Posit

from . import forms


@app.route('/', methods=['GET','POST'])
def index():
    form = forms.posit()
    if form.validate_on_submit():
        title = form.title.data
    return render_template('index.html',form=form, posits = Posit.query.order_by(Posit.date).all())


@app.route('/new_posit', methods=['GET','POST'])
def new_posit():
    form = forms.posit()
    date_act = datetime.date.today()
    if request.method == 'POST':
        new_posit = Posit(
                title = form.title.data,
                body = form.body.data,
                date = date_act,
                category = form.category.data,
                color = form.color.data
                )
        db.session.add(new_posit)
        db.session.commit()
        flash("Nota creada exitosamente","success")
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/posit_edit/<id>', methods=['GET','POST'])
def posit_edit(id):
    form = forms.posit()

    if request.method == 'GET':
        datos = Posit.query.get(id)
        form.title.data , form.body.data = datos.title , datos.body
        form.category.process_data(datos.category)
        form.color.process_data(datos.color)
        return render_template('posit_edit.html',datos=datos, form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            date = datetime.date.today()
        posit = Posit.query.get(id)

        posit.title = form.title.data
        posit.body = form.body.data
        posit.date = date
        posit.category = form.category.data
        posit.color = form.color.data
        db.session.commit()
        flash("Nota actualizada exitosamente","success")
        return redirect(url_for('index'))

@app.route('/delete_posit/<id>')
def delete_posit(id):
    posit_id = Posit.query.get(id)
    db.session.delete(posit_id)
    db.session.commit()
    flash("Nota eliminada exitosamente","success")
    return redirect(url_for('index'))

""" 
@app.route('/signin',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        user = request.form['user']
        password = generate_password_hash(request.form['password'])
        db.search_user(user,password)
        return render_template('signin.html')  

@app.route('/login', methods=['POST','GET'])
def login():
    form = forms.log_form()
    if request.method == 'POST':
        user = request.form['user']
        password = generate_password_hash(request.form['password'])
        print(user , password)
        return render_template('login.html',form=form)
"""
