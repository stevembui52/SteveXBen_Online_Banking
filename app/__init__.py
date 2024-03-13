from flask import Flask, render_template
from all_apis.customer_api import customer
from all_apis.branch_api import branch
from all_apis.account_api import account
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECTRET_KEY'] = '0974ad8cfe75e7da6ed536f9'
    app.config['JWT_SECRET_KEY'] = 'a06a72bff1fd7c19ff81895356b5f29b'
    @app.route("/")
    def index():
        return render_template("index.html")
    
    JWTManager(app)
    
    app.register_blueprint(customer)
    app.register_blueprint(branch)
    app.register_blueprint(account)

    return app




if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
