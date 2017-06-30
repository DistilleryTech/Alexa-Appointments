from flask import Blueprint, render_template
from flask_ask import Ask, session, question, statement
from models import Appointment
from forms import  AppointmentForm

blueprint = Blueprint('blueprint_api', __name__, url_prefix="/")
ask = Ask(blueprint=blueprint)

from . import launch, new_appointment
