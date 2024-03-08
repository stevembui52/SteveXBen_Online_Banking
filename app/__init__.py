from flask import Flask
from customer_api import customer
from branch_api import branch
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config['SECTRET_KEY'] = '0974ad8cfe75e7da6ed536f9'
    app.config['JWT_SECRET_KEY'] = 'a06a72bff1fd7c19ff81895356b5f29b'
    @app.route("/")
    def index():
        return {"message": "hello children"}
    
    JWTManager(app)
    
    app.register_blueprint(customer)
    app.register_blueprint(branch)

    return app




if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
