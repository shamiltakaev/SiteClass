from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[])
    password = PasswordField('Пароль', validators=[])
    password_again = PasswordField('Повторите пароль', validators=[])
    name = StringField('Имя пользователя', validators=[])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


    def __init__(self, *args, **kwargs):
        kwargs["csrf_enabled"] = False
        super(RegisterForm, self).__init__(args, kwargs)