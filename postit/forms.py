from flask_wtf import FlaskForm
from wtforms import Form, IntegerField, SelectField, SubmitField, StringField, PasswordField
from wtforms.validators import Required , DataRequired
from wtforms.widgets import TextArea


class posit(FlaskForm):
    title = StringField("Titulo del Posit",validators=[DataRequired()])
    body = StringField(u'Contenido del Posit', widget=TextArea())
    category = SelectField("Seleccione la categoria",
                            choices=[
                                ("Importante","Importante"),
                                ("Programacion","Programacion"),
                                ("Pyhton","Python")],
                            )
    color = SelectField("Seleccione un color",
                            choices=[
                                ("bg-primary","Azul"),
                                ("bg-danger","Rojo"),
                                ("bg-success","Verde"),
                                ("bg-warning","Naranja"),
                                ])
    submit = SubmitField("Crear")

class log_form(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
