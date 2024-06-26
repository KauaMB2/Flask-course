from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')
    def validate_email_address(self, email_address_to_check):
        user=User.query.filter_by(email_address=email_address_to_check.data).first()
        if user:
            raise ValidationError('Email address already exists! Please try a different Email address')

    username=StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address=StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1=PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2=PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username=StringField(label='User Name:',validators=[DataRequired()])
    password=StringField(label='Password:',validators=[DataRequired()])
    submit=SubmitField(label='Sign in')

class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit=SubmitField(label='Sell Item!')

class CommentItemForm(FlaskForm):
    comment_input=StringField(label='Add a comment:', validators=[Length(min=5, max=100), DataRequired()])
    submit=SubmitField(label='Comment!')

class AddItemForm(FlaskForm):
    name=StringField(label='Product Name:', validators=[Length(min=2, max=30), DataRequired()])
    price=StringField(label='Price:', validators=[DataRequired()])
    barcode=StringField(label='Barcode:', validators=[Length(min=12,max=12), DataRequired()])
    description=StringField(label='Description:', validators=[DataRequired()])
    submit=SubmitField(label='Create Item!')






