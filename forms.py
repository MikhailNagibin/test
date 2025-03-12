from wtforms import *
from flask_wtf import *
from wtforms.validators import *

class AutorisationForm(FlaskForm):
    email = EmailField("Введите Вашу почту", validators=[DataRequired()])
    password = PasswordField("Введите Ваш пароль", validators=[DataRequired()])
    submit = SubmitField("Войти")