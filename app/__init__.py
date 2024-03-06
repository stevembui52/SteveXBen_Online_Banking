from flask import Flask
from .customer_api import customer

def create_app(app_config = True):

    app = Flask(__name__)


    app.register_blueprint(customer)

    return app