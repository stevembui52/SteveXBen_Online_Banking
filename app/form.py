from wtforms import Form, FloatField, SelectField, StringField, PasswordField, TextAreaField, validators, IntegerField
from wtforms.validators import NumberRange

choices=[('current', 'Current Account'), ('saving', 'Savings account'), 
        ('Fixed deposits', 'fixed deposits'), ('shares', 'Share capital')]
class RegisterForm(Form):
    first_name = StringField('FirstName', [validators.Length(max=30, min=4)])
    last_name = StringField('LastName', [validators.Length(max=30, min=4)])
    username = StringField('Username', [validators.length(max=15, min=3)])
    id_number = IntegerField('IdNumber', [validators.DataRequired()])
    email = StringField('Email', [validators.Length(max=20, min=7)])
    address = StringField('Address', [validators.Length(max=20, min=7)])
    phone_no = IntegerField('PhoneNo', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(),
                            validators.EqualTo('confirm', message="passwords don't match")])
    confirm = PasswordField('Confirm Password')

class LoginForm(Form):
    username = StringField('Username', [validators.length(max=15, min=3)])
    password = PasswordField('Password', [validators.DataRequired()])

class AccountForm(Form):
    account_number = StringField('AccountNumber', [validators.DataRequired()])
    account_type = SelectField('AcccountType', [validators.DataRequired()], choices=choices )
    balance = FloatField('Balance', [validators.DataRequired(), NumberRange(min=0)])
