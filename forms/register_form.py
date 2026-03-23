from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from forms.login_form import LoginForm


class RegisterForm(LoginForm):
    surname = StringField("Surname")
    name = StringField("Name")
    age = IntegerField("Age")
    position = StringField("Position")
    speciality = StringField("Speciality")
    address = StringField("Address")
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")
