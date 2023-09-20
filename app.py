from flask import Flask, request, jsonify
from mongodb import initialize_mongodb  # Import MongoDB functions
from flask_cors import CORS
from auth import auth_bp, initialize_jwt  # Import the auth blueprint
from hotel import Hotel
from staff import Staff
from booking import Booking
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity




app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/auth")

# MongoDB configuration
initialize_mongodb(app)  # Initialize MongoDB connection

# Initilize JWT
initialize_jwt(app)

# Set CORS headers for the entire Flask application
CORS(app, origins=["http://localhost:3000"])


# Endpoint to get a list of available hotels

@app.route("/api/hotels", methods=["GET"])
def get_hotels():
    #  data = request.get_json()
     hotelList = Hotel.get_hotel_by_page(1,20)
     print("hotelList",hotelList)
     return jsonify({"data":hotelList,"status":200})

# Endpoint to book a hotel room
@jwt_required()
@app.route("/api/bookings", methods=["POST"])
def book_hotel():
    data = request.get_json()
    hotel_id = data.get("hotel_id")
    check_in = data.get("check_in")
    check_out = data.get("check_out")

    # Insert the booking data into MongoDB
    # booking_id = insert_booking(hotel_id, check_in, check_out)

    return jsonify({"message": "Booking successful!", "booking_id": "under development", "status": 200})


# Endpoint to book a hotel room

@app.route("/api/createHotel", methods=["POST"])
@jwt_required()
def create_hotel():
     try:
        current_user = get_jwt_identity()
        if not current_user:
            return jsonify({"message": "Invalid token", "status": 401})
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        price_per_24Hrs = data.get("price_per_24Hrs")
        location = data.get("location")
        amenities = data.get("amenities")
        contact_number = data.get("contact_number")
        hotelID = data.get("hotelID")
        contactname = data.get("contactname")
        # Insert the booking data into MongoDB
        result = Hotel.create_hotel(name,description,price_per_24Hrs,location,amenities,contactname,contact_number,hotelID)

        return jsonify(result)
     except Exception as e:
        return jsonify({"error": str(e), "status": 500})


if __name__ == "__main__":
    app.run(debug=True)
