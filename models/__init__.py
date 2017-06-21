from flask_mongoengine import MongoEngine

db = MongoEngine()

from .appointment import Appointment
