from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, SubmitField, validators
from wtforms.validators import Email, Length, DataRequired, EqualTo, ValidationError


from .models import User


class RegsiterForm(FlaskForm):

    name = StringField(label='Name', validators=[DataRequired(), Length(min=9, max=20)])
    email = StringField(label="Email Address", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=7, max=17)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), Length(min=7, max=17), EqualTo('password')])
    submit = SubmitField(label="Register")

    # own custom validator should have name validate_{{fieldName}}
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("User already exists.")


class LoginForm(FlaskForm):

    email = StringField(label="Email Address", validators=[Email(), DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=7, max=17)])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField(label="Login")

    
    ## validations done using flash messaging
        
