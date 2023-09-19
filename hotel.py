from mongoengine import Document, StringField, FloatField, ReferenceField
from staff import Staff


class Hotel(Document):
    name = StringField(required=True, max_length=100)
    description = StringField()
    price_per_24Hrs = FloatField(required=True, min_value=0)
    location = StringField()
    amenities = StringField()
    contact_person = ReferenceField(Staff)
    contact_number = StringField()
    hotelID = StringField(required=True)

    # def __str__(self):
    #     return f"{self.name} ({self.location}): ${self.price_per_24Hrs} per night"

    @classmethod
    def create_hotel( cls, name, description, price_per_24Hrs, location, amenities, contact_person, contact_number, hotelID):
        try:
            hotel = cls(
                name=name,
                description=description,
                price_per_24Hrs=price_per_24Hrs,
                location=location,
                amenities=amenities,
                # contact_person=contact_person,
                contact_number=contact_number,
                hotelID=hotelID
            )
            hotel.save()
            return {"message": "Hotel created successfully"}
        except Exception as e:
            return {"error": str(e),"data":name}

    @classmethod
    def get_hotel_by_id(cls, hotel_id):
         hotelObj = cls.objects(hotelID=hotel_id).first()
         hotel_data = {"name": hotelObj.name, "description": hotelObj.description, "price_per_24Hrs": hotelObj.price_per_24Hrs, "location": hotelObj.location, "amenities": hotelObj.amenities} 
         return hotel_data
    
    @classmethod
    def get_hotel_by_page(cls, pageNo, pageLimit):
        # Calculate the number of documents to skip based on the page number and limit
        skip_count = (pageNo - 1) * pageLimit

        # Use the `skip` and `limit` methods to fetch data page and limit-wise
        hotels = cls.objects.skip(skip_count).limit(pageLimit)
        hotel_data = [{"name": hotel.name, "description": hotel.description, "price_per_24Hrs": hotel.price_per_24Hrs, "location": hotel.location, "amenities": hotel.amenities} for hotel in hotels]

        return hotel_data

    @classmethod
    def update_hotel(cls, hotel_id, **update_data):
        hotel = cls.get_hotel_by_id(hotel_id)
        if hotel:
            for key, value in update_data.items():
                setattr(hotel, key, value)
            hotel.save()

    @classmethod
    def delete_hotel(cls, hotel_id):
        hotel = cls.get_hotel_by_id(hotel_id)
        if hotel:
            hotel.delete()
