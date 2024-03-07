from flask import Flask
from customer_api import customer
from branch_api import branch

def create_app(app_config=None):

    app = Flask(__name__)

    @app.route("/")
    def index():
        return {"message": "hello children"}
    
    app.register_blueprint(customer)
    app.register_blueprint(branch)

    return app




if __name__ == "__main__":
    app = create_app(None)
    app.run(debug=True)
