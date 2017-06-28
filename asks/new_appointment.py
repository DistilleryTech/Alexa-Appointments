from flask import render_template
from flask_ask import question, statement
import ipdb
from . import ask

@ask.intent("CuragoAppointmentIntent")
def create_appointment():
    msg = render_template('date')
    return question(msg)

@ask.intent("CuragoAppointmentDateIntent", convert={'begin_date': 'date'})
def appointment_date(begin_date):
    qs = render_template('time')
    return question(qs)

@ask.intent("CuragoAppointmentTimeIntent", convert={'begin_time': 'time'})
def appointment_time(begin_time):
    msg = render_template('end_date')
    return question(msg)

@ask.intent("CuragoAppointmentEndDateIntent", convert={'end_date': 'date'})
def appointment_end_date(end_date):
    msg = render_template('end_time')
    return question(msg)

@ask.intent("CuragoAppointmentEndTimeIntent", convert={'end_time': 'time'})
def appointment_end_time(end_time):
    msg = render_template('created_succesfully')
    return statement(msg)

@ask.intent("CuragoAppointmentWithBeginDateAndTimeIntent", convert={'begin_date': 'date', 'begin_time': 'time'})
def appointment_with_begin_date(begin_date, begin_time):
    msg = render_template('end_date')
    print('CuragoAppointmentWithBeginDateAndTimeIntent', msg)
    return question(msg)

@ask.intent("CuragoAppointmentWithEndDateAndTimeIntent", convert={'end_date': 'date', 'end_time': 'time'})
def appointment_with_end_date(end_date, end_time):
    print('CuragoAppointmentWithEndDateAndTimeIntent', end_date, end_time)
    msg = render_template('created_succesfully')
    return statement(msg)
