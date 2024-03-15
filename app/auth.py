from flask import Blueprint, request, render_template, flash, redirect, url_for
from db_model import *
from form import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_jwt_extended import create_refresh_token, create_access_token, jwt_required, get_jwt_identity

local_session = Session(bind=engine)

customers = Blueprint("customers", __name__)


@customers.route("/register", methods = ["POST", "GET"])
def create_customer():
    form = RegisterForm(request.form)
    if request.method == "POST" and  form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        id_number = form.id_number.data
        email = form.email.data
        # branch_id = data["branch_id"]
        # account_id = data["account_id"]
        phone_no = form.phone_no.data
        password = form.password.data
        address = form.address.data

        user = local_session.query(Customer).filter(Customer.username==username).first()

        if user:
            flash('Already registered please login ', 'danger')
            return render_template("register.html", form=form)

        hashed_pwd = generate_password_hash(password)

        cust = Customer(first_name=first_name, last_name=last_name, username=username,
                        id_number=id_number, email=email, phone_no=phone_no,
                        password=hashed_pwd, address=address)
        
        local_session.add(cust)
        local_session.commit()
        flash('You are now registered you can login', 'success')
        return redirect(url_for("index"))
    return render_template("register.html", form=form)
    


@customers.route("/login", methods = ["POST", "GET"])
def cust_login():
    form = LoginForm(request.form)
    if request.method=="POST":
        username = form.username.data
        pass_cand = form.password.data

        user = local_session.query(Customer).filter(Customer.username==username).first()

        if user:
            if check_password_hash(user.password, pass_cand):
                flash("log in successiful", "success")
                return redirect(url_for("about"))
            else:
                flash("incorrect creds", "danger")
                return render_template("login.html", form=form)
        else:
            flash("No such user", "warning")
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)