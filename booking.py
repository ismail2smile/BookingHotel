from mongoengine import Document, StringField, IntField, DateField, ObjectIdField,ReferenceField
from staff import Staff
from hotel import Hotel
from baseDocumentConfig import BaseDocument
import datetime


class Booking(BaseDocument):
    hotel_id = ReferenceField(Hotel)
    staff_id = ReferenceField(Staff)
    advanced_amount = IntField(required=True, min_value=0)
    booking_amount = IntField(required=True, min_value=0)
    bookie_name = StringField(required=True, min_length=2, max_length=50)
    bookie_number = StringField(required=True, min_length=2, max_length=15)
    bookie_alt_number = StringField(min_length=2, max_length=15)
    start_date = DateField()
    end_date = DateField()
    start_date = DateField()
    end_date = DateField()

    @classmethod
    def create_booking(cls, hotel_id, staff_id, advanced_amount, booking_amount, bookie_name, bookie_number, bookie_alt_number, start_date, end_date):
        booking = cls(
            hotel_id=hotel_id,
            staff_id=staff_id,
            advanced_amount=advanced_amount,
            booking_amount=booking_amount,
            bookie_name=bookie_name,
            bookie_number=bookie_number,
            bookie_alt_number=bookie_alt_number,
            start_date=start_date,
            end_date=end_date
        )
        booking.save()
        return booking

    @classmethod
    def get_booking_by_id(cls, booking_id):
        return cls.objects(id=booking_id).first()

    @classmethod
    def update_booking(cls, booking_id, **update_data):
        booking = cls.get_booking_by_id(booking_id)
        if booking:
            for key, value in update_data.items():
                setattr(booking, key, value)
            booking.save()

    @classmethod
    def delete_booking(cls, booking_id):
        booking = cls.get_booking_by_id(booking_id)
        if booking:
            booking.delete()
