from flask import Flask, render_template
from all_apis.customer_api import customer
from all_apis.branch_api import branch
from all_apis.account_api import account
from dashboard import dashboard
from flask_jwt_extended import JWTManager
from auth import customers
from is_logged import is_logged_in

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECTRET_KEY'] = '0974ad8cfe75e7da6ed536f9'
    app.config['JWT_SECRET_KEY'] = 'a06a72bff1fd7c19ff81895356b5f29b'
    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/about")
    @is_logged_in
    def about():
        return render_template("about.html")
    
    JWTManager(app)
    
    app.register_blueprint(customer)
    app.register_blueprint(branch)
    app.register_blueprint(account)
    app.register_blueprint(customers)
    app.register_blueprint(dashboard)
    return app




if __name__ == "__main__":
    app = create_app()
    app.secret_key="kkkkkk"
    app.run(debug=True)
