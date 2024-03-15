from functools import wraps
from flask import  session, url_for, redirect, flash

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return(f(*args, **kwargs))
        else:
            flash('Unauthorised, Please log in', 'danger')
            return redirect(url_for('customers.cust_login'))
    return wrap