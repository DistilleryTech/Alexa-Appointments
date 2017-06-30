from . import (ask, session, render_template, question, statement,
               Appointment, AppointmentForm, render_result)

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
    return question(msg)

@ask.intent("CuragoAppointmentEndDateIntent", convert={'end_date': 'date'})
def appointment_end_date(end_date):
    session.attributes['end_date'] = str(end_date)
    msg = render_template('end_time')
    return question(msg)

@ask.intent("CuragoAppointmentEndTimeIntent", convert={'end_time': 'time'})
def appointment_end_time(end_time):
    session.attributes['end_time'] = str(end_time)
    form = AppointmentForm(session.attributes)
    form.submit()
    render_result(form)
