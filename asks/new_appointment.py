from flask import render_template
from flask_ask import question, statement
import ipdb
from . import ask, session
from models import Appointment
from datetime import datetime

@ask.intent("CuragoAppointmentIntent")
def create_appointment():
    msg = render_template('date')
    return question(msg)

@ask.intent("CuragoAppointmentDateIntent", convert={'begin_date': 'date'})
def appointment_date(begin_date):
    session.attributes['begin_date'] = str(begin_date)
    qs = render_template('time')
    return question(qs)

@ask.intent("CuragoAppointmentTimeIntent", convert={'begin_time': 'time'})
def appointment_time(begin_time):
    session.attributes['begin_time'] = str(begin_time)
    print(session.attributes['begin_time'])
    return question(msg)

@ask.intent("CuragoAppointmentEndDateIntent", convert={'end_date': 'date'})
def appointment_end_date(end_date):
    session.attributes['end_date'] = str(end_date)
    msg = render_template('end_time')
    return question(msg)

@ask.intent("CuragoAppointmentEndTimeIntent", convert={'end_time': 'time'})
def appointment_end_time(end_time):
    session.attributes['end_time'] = str(end_time)
    full_begin_date = session.attributes['begin_date'] + ' ' + session.attributes['begin_time']
    full_end_date = session.attributes['end_date'] + ' ' + session.attributes['end_time']
    full_begin_datetime = datetime.strptime(full_begin_date, '%Y-%m-%d %H:%M:%S')
    full_end_datetime = datetime.strptime(full_end_date, '%Y-%m-%d %H:%M:%S')
    appointment = Appointment(begin_date=full_begin_datetime, end_date=full_end_datetime)
    appointment.save()
    msg = render_template('created_succesfully',
                          begin_date=appointment.begin_date.date(),
                          begin_time=appointment.begin_date.time(),
                          end_date=appointment.end_date.date(),
                          end_time=appointment.end_date.time())
    return statement(msg)


@ask.intent("CuragoAppointmentWithBeginDateAndTimeIntent",
            convert={'begin_date': 'date', 'begin_time': 'time'})
def appointment_with_begin_date(begin_date, begin_time):
    session.attributes['begin_date'] = str(begin_date)
    session.attributes['begin_time'] = str(begin_time)
    msg = render_template('end_date')
    return question(msg)

@ask.intent("CuragoAppointmentWithEndDateAndTimeIntent",
            convert={'end_date': 'date', 'end_time': 'time'})
def appointment_with_end_date(end_date, end_time):
    session.attributes['end_date'] = str(end_date)
    session.attributes['end_time'] = str(end_time)
    full_begin_date = session.attributes['begin_date'] + ' ' + session.attributes['begin_time']
    full_end_date = session.attributes['end_date'] + ' ' + session.attributes['end_time']
    full_begin_datetime = datetime.strptime(full_begin_date, '%Y-%m-%d %H:%M:%S')
    full_end_datetime = datetime.strptime(full_end_date, '%Y-%m-%d %H:%M:%S')
    appointment = Appointment(begin_date=full_begin_datetime, end_date=full_end_datetime)
    appointment.save()
    msg = render_template('created_succesfully',
                          begin_date=appointment.begin_date.date(),
                          begin_time=appointment.begin_date.time(),
                          end_date=appointment.end_date.date(),
                          end_time=appointment.end_date.time())
    return statement(msg)

@ask.intent("CuragoAppointmentWithFullDataIntent",
            convert={'begin_date': 'date', 'begin_time': 'time',
                     'end_date': 'date', 'end_time': 'time'})
def appointment_with_full_date(begin_date, begin_time, end_date, end_time):
    session.attributes['begin_date'] = str(begin_date)
    session.attributes['begin_time'] = str(begin_time)
    session.attributes['end_date'] = str(end_date)
    session.attributes['end_time'] = str(end_time)
    full_begin_date = str(begin_date) + ' ' + str(begin_time)
    full_end_date = str(end_date) + ' ' + str(end_time)
    full_begin_datetime = datetime.strptime(full_begin_date, '%Y-%m-%d %H:%M:%S')
    full_end_datetime = datetime.strptime(full_end_date, '%Y-%m-%d %H:%M:%S')
    appointment = Appointment(begin_date=full_begin_datetime, end_date=full_end_datetime)
    appointment.save()
    msg = render_template('created_succesfully',
                          begin_date=appointment.begin_date.date(),
                          begin_time=appointment.begin_date.time(),
                          end_date=appointment.end_date.date(),
                          end_time=appointment.end_date.time())
    return statement(msg)

@ask.intent("AMAZON.HelpIntent")
def help_intent():
    return statement('help')

@ask.intent("AMAZON.AddAction<object@Event>", mapping={
        'ownerName': 'object.owner.name',
        'collection_owner_name': 'targetCollection.owner.name',
        'object_start_date': 'object.startDate',
        'object_type': 'object.type',
        'object_name': 'object.name',
        'object_start_time': 'object.startTime',
        'object_attendee_name': 'object.attendee.name',
        'object_decription_type': 'object.description.type',
        'target_collection_type': 'targetCollection.type',
        'object_event_type': 'object.event.type'
})
def add_new_object(ownerName, collection_owner_name, object_start_date,
                   object_type, object_name, object_start_time,
                   object_attendee_name, object_decription_type,
                   target_collection_type, object_event_type):
    if object_start_date is None:
        return question('date')
    if object_start_time is None:
        return question('time')
    # ipdb.set_trace()
    # msg = render_template('created_succesfully')
    # return statement(msg)
