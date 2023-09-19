from flask_pymongo import PyMongo
from mongoengine import Document, StringField, FloatField, ReferenceField, connect
mongo = PyMongo()
baseurl = 'mongodb://localhost:27017/hotelApp'

def initialize_mongodb(app):
    # Configure MongoDB connection using app's configuration
    print("app Mongo initialize")
    app.config['MONGO_URI'] = baseurl
    mongo.init_app(app)
    connect(host=baseurl)



# Specify which functions should be exported
__all__ = ["initialize_mongodb"]
