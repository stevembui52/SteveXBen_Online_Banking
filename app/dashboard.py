from flask import Blueprint, request, render_template, flash, redirect, url_for, session



dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def dashboard():
    return render_template("dashboard.html")