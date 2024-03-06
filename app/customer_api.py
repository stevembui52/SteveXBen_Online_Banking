from flask import Blueprint


customer = Blueprint("customer", __name__, url_prefix="/api/v1/customer")


@customer.route("/")
def create_customer():
    pass


@customer.route("/login")
def cust_login():
    pass

