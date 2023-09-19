from flask import Blueprint, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import random

# Define the range (inclusive)
min_value = 0
max_value = 7  # Change these values as needed

# Generate a random number within the specified range


auth_bp = Blueprint("auth", __name__)
CORS(auth_bp, resources={r"/login": {"origins": "http://localhost:3000"}})

api = Api(auth_bp)

# In-memory user data (replace this with a database in production)
users = {
    "user1": {"username": "user1", "password": "password1"},
    "user2": {"username": "user2", "password": "password2"},
}

# Token-based authentication (for simplicity, use hardcoded tokens)
tokens = {
    "0": "af1d1d1f-a1d7-4f56-a366-028fd14f2c5c",
    "1": "0c63cebb-9ee7-420f-9482-e45512ee682b",
    "2": "7d53fd84-efb1-4559-ab25-0297287d454d",
    "3": "26c42937-7da2-46c2-85b9-31172503f68f",
    "4": "34b95e08-dfaf-4988-a896-5442452215ae",
    "5": "3da96e95-c797-4408-adf5-f4ce851c7225",
    "6": "a5489ac3-628c-4373-9813-0a097ae9a20d",
    "7": "edc7c660-dd02-42d4-b3ab-fcb89059e3c9",
}



class Login(Resource):
    def post(self):
        data = request.get_json()
        print("login data", data)

        username = data.get('username')
        password = data.get('password')

        # Check if the username exists and the provided password matches
        if username in users and users[username]['password'] == password:
            random_number = random.randint(min_value, max_value)
            token = tokens[str(random_number)]
            response = jsonify({"message": "Login successful", "token" : token,"status":200})
            response.status_code = 200
        else:
            response = jsonify({"message": "Login failed","status":401})
            response.status_code = 401

        return response

api.add_resource(Login, "/login")
