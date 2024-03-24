from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from is_logged import is_logged_in
from db_model import *

localsession =Session(bind=engine)


dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
@is_logged_in
def dashboard_func():
    result = localsession.query(Account).all()

    if result:
        account = result
        return render_template('dashboard.html', account=account)
    return render_template("dashboard.html")