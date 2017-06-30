from flask import Blueprint, render_template
from flask_ask import Ask, session, question, statement
from models import Appointment
from forms import  AppointmentForm

blueprint = Blueprint('blueprint_api', __name__, url_prefix="/")
ask = Ask(blueprint=blueprint)

def render_result(form):
    """ render statement with appointment information """
    msg = render_template('created_succesfully',
                          begin_date=form.appointment.begin_date.date(),
                          begin_time=form.appointment.begin_date.time(),
                          end_date=form.appointment.end_date.date(),
                          end_time=form.appointment.end_date.time()
    )
    return statement(msg)

from . import (launch, all_steps_workflow,
               two_steps_workflow, one_step_workflow)
