from mongoengine import Document, DateTimeField, BooleanField
import datetime

class BaseDocument(Document):
    meta = {'allow_inheritance': True}
    created_on = DateTimeField()
    modified_on = DateTimeField()
    deleted = BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.created_on:
            self.created_on = datetime.datetime.now()
        self.modified_on = datetime.datetime.now()
        super(BaseDocument, self).save(*args, **kwargs)
