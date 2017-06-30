from . import db

class Appointment(db.Document):
    """ Appointment object presentation """

    text = db.StringField(max_length=255)
    begin_date = db.DateTimeField()
    end_date = db.DateTimeField()
