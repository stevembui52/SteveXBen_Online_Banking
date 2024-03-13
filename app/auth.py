from flask import Blueprint, request
from db_model import *
from forms import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_jwt_extended import create_refresh_token, create_access_token, jwt_required, get_jwt_identity

local_session = Session(bind=engine)

customers = Blueprint("customers", __name__, url_prefix="/api/v1/customers")


@customers.route("/register", methods = ["POST", "GET"])
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
            return 
        if len(last_name) < 3:
            return 
        if len(username) < 3:
            return 
        if not username.isalnum() or " " in username:
            return 
        # if len(id_number) < 6 and len(id_number) > 8:
        #     return jsonify({"warning":"invalid id number"})
        if user.username == username:
            return 
        # if user.id_number == id_number:
        #     return jsonify({"warning":"Identification already in use"})
        hashed_pwd = generate_password_hash(password)

        cust = Customer(first_name=first_name, last_name=last_name, username=username,
                        id_number=id_number, email=email, phone_no=phone_no,
                        password=hashed_pwd, address=address)
        
        local_session.add(cust)
        local_session.commit()

        return 
    


@customers.route("/login", methods = ["POST"])
def cust_login():
    if request.method=="POST":
        user_name = request.json.get("user_name")
        password = request.json.get("password")

        user = local_session.query(Customer).filter(Customer.username==user_name).first()

        if user:
            if check_password_hash(user.password, password):
                pass
    