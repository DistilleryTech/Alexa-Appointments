from flask import Blueprint, render_template
from flask_ask import Ask, session, question, statement
from models import Appointment
from forms import  AppointmentForm

blueprint = Blueprint('blueprint_api', __name__, url_prefix="/")
ask = Ask(blueprint=blueprint)

def render_result(form):
    msg = render_template('created_succesfully',
                          begin_date=appointment.begin_date.date(),
                          begin_time=appointment.begin_date.time(),
                          end_date=appointment.end_date.date(),
                          end_time=appointment.end_date.time())
    return statement(msg)

from . import launch, new_appointment, all_steps_workflow, two_steps_workflow
