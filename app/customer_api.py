from flask import Blueprint, request, jsonify
from db_model import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_refresh_token, create_access_token

local_session = Session(bind=engine)

customer = Blueprint("customer", __name__, url_prefix="/api/v1/customer")


@customer.route("/register", methods = ["POST", "GET"])
def create_customer():
    if request.method == "POST":
        data = request.get_json()
        first_name = data["first_name"]
        last_name = data["last_name"]
        username = data["username"]
        id_number = data["id_number"]
        email = data["email"]
        # branch_id = data["branch_id"]
        # account_id = data["account_id"]
        phone_no = data["phone_no"]
        password = data["password"]
        address = data["address"]

        user = local_session.query(Customer).filter(Customer.username==username).first()

        if len(first_name) < 3:
            return jsonify({"Warning": "first name short!"}), 401
        if len(last_name) < 3:
            return jsonify({"Warning": "last name short!"}), 401
        if len(username) < 3:
            return jsonify({"Warning": "username name short!"}), 401
        if not username.isalnum() or " " in username:
            return jsonify({"Warning": "Invalid username"}), 401
        # if len(id_number) < 6 and len(id_number) > 8:
        #     return jsonify({"warning":"invalid id number"})
        if user.username == username:
            return jsonify({"warning":"Username already exists"}), 409
        # if user.id_number == id_number:
        #     return jsonify({"warning":"Identification already in use"})
        hashed_pwd = generate_password_hash(password)

        cust = Customer(first_name=first_name, last_name=last_name, username=username,
                        id_number=id_number, email=email, phone_no=phone_no,
                        password=hashed_pwd, address=address)
        
        local_session.add(cust)
        local_session.commit()

        return jsonify({"Message":"User Created Successifully",
                        "Customer":{"username":username,
                                    "email":email,
                                    "phone_number":phone_no,
                                    "address":address}}), 201
    


@customer.route("/login", methods = ["POST"])
def cust_login():
    if request.method=="POST":
        user_name = request.json.get("user_name")
        password = request.json.get("password")

        user = local_session.query(Customer).filter(Customer.username==user_name).first()

        if user:
            if check_password_hash(user.password, password):
                access = create_access_token(identity=user.id)
                refresh = create_refresh_token(identity=user.id)
                return jsonify({"Message": "User logged in successifully",
                                "Access":access,
                                "refresh":refresh}), 200
            else:
                return jsonify({"Error":"invalid credentials"}), 401
        else:
            return jsonify({"Error":"User not found"}), 404