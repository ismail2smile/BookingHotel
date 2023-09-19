from mongoengine import Document, StringField, FloatField, IntField,ReferenceField
from baseDocumentConfig import BaseDocument
import datetime


class Staff(BaseDocument):
    first_name = StringField(required=True, max_length=15)
    last_name = StringField(required=True, max_length=15)
    full_name = StringField(required=True, max_length=50)
    age = IntField(required=True, min_value=18)
    experience = IntField(required=True, min_value=0)
    higestQualification = StringField()
    role_position = StringField()
    empID = StringField()

    def __str__(self):
        return f"{self.full_name} (Age: {self.age}, Experience: {self.experience} years)"

    @classmethod
    def create_staff(cls, first_name, last_name, full_name, age, experience, higestQualification, role_position, empID):
        staff = cls(
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            age=age,
            experience=experience,
            higestQualification=higestQualification,
            role_position=role_position,
            empID=empID
        )
        staff.save()
        return staff

    @classmethod
    def get_staff_by_id(cls, emp_id):
        return cls.objects(empID=emp_id).first()

    @classmethod
    def update_staff(cls, emp_id, **update_data):
        staff = cls.get_staff_by_id(emp_id)
        if staff:
            for key, value in update_data.items():
                setattr(staff, key, value)
            staff.save()

    @classmethod
    def delete_staff(cls, emp_id):
        staff = cls.get_staff_by_id(emp_id)
        if staff:
            staff.delete()
