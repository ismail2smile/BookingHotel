from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from flask_cors import CORS
import random

auth_bp = Blueprint("auth", __name__)
CORS(auth_bp, resources={r"/login": {"origins": "http://localhost:3000"}})

# In-memory user data (replace this with a database in production)
users = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"},
}

# Initialize JWTManager
jwt = JWTManager()

# Initialize JWT configuration
def initialize_jwt(app):
    app.config['JWT_SECRET_KEY'] = 'cb454e36-d3ad-45c5-96cd-0c6eb9f3e02e'  # Change this to your secret key
    jwt.init_app(app)

# Login route
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Check if the username and password are valid (you can add your authentication logic here)
    if username in users and users[username]["password"] == password:
        # Generate an access token
        random_number = random.randint(0, 7)  # Adjust the range as needed
        access_token = create_access_token(identity=username, additional_claims={"random_number": random_number})

        return jsonify({"message": "Login successful", "access_token": access_token, "status": 200})
    else:
        return jsonify({"message": "Login failed", "status": 401})
