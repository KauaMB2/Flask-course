from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
	username=StringField(label='User Name:')#label="(Título secundário)
	email_address=StringField(label='Email Address:')#label="(Título secundário)
	password1=PasswordField(label='Password:')#label="(Título secundário)
	password2=PasswordField(label='Confirm Password:')#label="(Título secundário)
	submit=SubmitField(label='Create Account')#label="(Título secundário)


