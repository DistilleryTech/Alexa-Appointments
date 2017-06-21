from . import db

class Appointment(db.Document):
    text = db.StringField(max_length=255)
    begin_date = db.DateTimeField()
    end_date = db.DateTimeField()
