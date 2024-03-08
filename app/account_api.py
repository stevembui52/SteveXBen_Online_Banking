from flask import Blueprint, request, jsonify
from db_model import *

local_session = Session(bind=engine)

account = Blueprint("account", __name__, url_prefix="/api/v1/account")


@account.route("/", methods = ["POST", "GET"])
def create_branch():
    if request.method == "POST":
        data = request.get_json()
        branch_name = data["branch_name"]
        branch_location = data["branch_location"]

        in_branch = local_session.query(Branch).filter_by(branch_name=branch_name).first()

        bran = Branch(branch_name=branch_name, branch_location=branch_location)
        
        local_session.add(bran)
        local_session.commit()

        return jsonify({"Message":"Branch Created Successifully",
                        "Branch":{"Branch name":branch_name,
                                    "branch location":branch_location}})