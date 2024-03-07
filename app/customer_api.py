from flask import Blueprint, request, jsonify
from .db_model import *
from werkzeug.security import generate_password_hash, check_password_hash

local_session = Session(bind=engine)

customer = Blueprint("customer", __name__, url_prefix="/api/v1/customer")


@customer.route("/", methods = ["POST", "GET"])
def create_customer():
    if request.method == "POST":
        data = request.json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        id_number = data.get("id_number")
        email = data.get("email")
        phone_no = data.get("phone_number")
        password = data.get("password")
        address = data.get("address")

        user = local_session.query(Customer).filter_by(username=username, id_number=id_number).first()

        if len(first_name) or len(last_name) or len(username) < 3:
            return jsonify({"Warning": "Too short!"})
        if not username.isalnum() or " " in username:
            return jsonify({"Warning": "Invalid username"})
        if len(id_number) < 6 and len(id_number) > 8:
            return jsonify({"warning":"invalid id number"})
        if user.username == username:
            return jsonify({"warning":"Username already exists"})
        if user.id_number == id_number:
            return jsonify({"warning":"Identification already in use"})
        hashed_pwd = generate_password_hash(password)

        cust = Customer(first_name=first_name, last_name=last_name, username=username,
                        id_number=id_number, email=email, phone_no=phone_no, password=hashed_pwd,
                        address=address)
        
        local_session.add(cust)
        local_session.commit()

        return jsonify({"Message":"User Created Successifully",
                        "Customer":{"username":username,
                                    "email":email,
                                    "phone_number":phone_no,
                                    "address":address}})
    


@customer.route("/login")
def cust_login():
    pass

