from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length , EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user :
            raise ValidationError('Username already exists! Please try a different username.')
        
    def validate_email_address(self, email_address_to_check):
        user = User.query.filter_by(email_address=email_address_to_check.data).first()
        if user :
            raise ValidationError('Email already exists! Please try a Email Address.')
        

    username = StringField(label='Enter your User Name', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Enter your Email address', validators=[Email(), Length(max=50), DataRequired()])
    password1 = PasswordField(label='Enter your Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Your Password', validators= [EqualTo('password1', message='Passwords must match'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='Enter your User Name', validators=[DataRequired()])
    password = PasswordField(label='Enter your Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item')


class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')  