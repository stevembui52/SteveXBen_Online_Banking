from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from is_logged import is_logged_in


dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
@is_logged_in
def dashboard_func():
    return render_template("dashboard.html")