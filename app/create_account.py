from flask import Blueprint, request, render_template, flash, redirect, url_for, session
from is_logged import is_logged_in
from db_model import *
from form import AccountForm
from flask_jwt_extended import get_jwt_identity, jwt_required
local_session =Session(bind=engine)


createacc = Blueprint("create_acc", __name__)

@createacc.route("/create_acc", methods=["GET", "POST"])
@is_logged_in
def create_acc():
    form = AccountForm(request.form)
    if request.method == "POST" and form.validate():
        account_number = form.account_number.data
        account_type = form.account_type.data
        balance = form.balance.data

        user = local_session.query(Customer).filter(Customer.id).first()
        print(user.id)
        if user:
            account = Account(account_number=account_number, 
                            account_type=account_type, balance=balance, user=user)
            
            local_session.add(account)
            local_session.commit()

        flash("account created successifully", "success")
        return redirect(url_for("dashboard.dashboard_func"))
    return render_template("create_acc.html", form=form)