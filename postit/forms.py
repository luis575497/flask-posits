from flask_wtf import FlaskForm
from wtforms import Form, IntegerField, SelectField, SubmitField, StringField, PasswordField
from wtforms.validators import Required , DataRequired, InputRequired, Email, EqualTo, Length
from wtforms.widgets import TextArea


class posit(FlaskForm):
    """Formulario para la creacion y modificacion de posits"""
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
    """Formulario para iniciar sesión de usuario, se establecen las respectivas validaciones para cada campo"""
    email = StringField("Email", validators=[DataRequired(),Email(message="Introduzca un correo válido")], render_kw={"placeholder":"Email"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder":"Password"})
    submit = SubmitField("Login")


class signup_form(FlaskForm):
    """Formulario para crear la cuenta de usuario, se valida cada campo según corresponda el tipo de datos"""
    name = StringField("Name", validators=[DataRequired()],render_kw={"placeholder": "Name"})
    email = StringField("Email", validators=[Email(message="Intruduzca un correo valido")], render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8,message="La contraseña debe ser de 8 caracteres minimo"), EqualTo('confirm', message="Las contraseñas no coinciden")], render_kw={"placeholder": "Password"})
    confirm = PasswordField("Repeat password", validators=[InputRequired()], render_kw={"placeholder": "Repeat password"})
    submit = SubmitField("Sign Up")
