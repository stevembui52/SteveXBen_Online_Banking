from wtforms import Form, StringField, PasswordField, TextAreaField, validators, IntegerField

class RegisterForm(Form):
    first_name = StringField('FirstName', [validators.Length(max=30, min=4)])
    last_name = StringField('LastName', [validators.Length(max=30, min=4)])
    username = StringField('Username', [validators.length(max=15, min=3)])
    id_number = IntegerField('IdNumber', [validators.length(max=15, min=3)])
    email = StringField('Email', [validators.Length(max=20, min=7)])
    address = StringField('Address', [validators.Length(max=20, min=7)])
    phone_no = IntegerField('PhoneNo', [validators.length(max=15, min=3)])
    password = PasswordField('Password', [validators.DataRequired(),
                              validators.EqualTo('confirm', message="passwords don't match")])
    confirm = PasswordField('Confirm Password')