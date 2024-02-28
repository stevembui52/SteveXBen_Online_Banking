from flask import Flask

def create_app(app_config = True):

    app = Flask(__name__)

    return app