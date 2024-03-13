from wtforms import Form, StringField, PasswordField, TextAreaField, validators

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(max=30, min=4)])
    username = StringField('Username', [validators.length(max=15, min=3)])
    email = StringField('Email', [validators.Length(max=20, min=7)])
    password = PasswordField('Password', [validators.DataRequired(),
                              validators.EqualTo('confirm', message="passwords don't match")])
    confirm = PasswordField('Confirm Password')