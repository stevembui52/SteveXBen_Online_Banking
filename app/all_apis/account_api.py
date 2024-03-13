from flask import Blueprint, request, jsonify
from db_model import *

local_session = Session(bind=engine)

account = Blueprint("account", __name__, url_prefix="/api/v1/account")


@account.route("/", methods = ["POST", "GET"])
def create_branch():
    if request.method == "POST":
        data = request.get_json()
        account_number = data["account_number"]
        account_type = data["account_type"]
        balance = data["balance"]

        # acc = local_session.query(Account).filter(Account.name).first()

        acc = Account(account_number=account_number, account_type=account_type,
                      balance=balance)
        
        local_session.add(acc)
        local_session.commit()

        return jsonify({"Message":"Account Created Successifully",
                        "Account":{"Account number":account_number,
                                    "Account type":account_type,
                                    "balance":balance}}), 201