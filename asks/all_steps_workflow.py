from . import (ask, session, render_template, question, statement,
               Appointment, AppointmentForm, render_result)

@ask.intent("CMAppointmentIntent")
def create_appointment():
    """ Initialize appointment's creation workflow; Pass to date definition """

    msg = render_template('date')
    return question(msg)

@ask.intent("CMAppointmentDateIntent", convert={'begin_date': 'date'})
def appointment_date(begin_date):
    """ Set appointment's begin date; Pass to appointment's begin time """

    session.attributes['begin_date'] = str(begin_date)
    qs = render_template('time')
    return question(qs)

@ask.intent("CMAppointmentTimeIntent", convert={'begin_time': 'time'})
def appointment_time(begin_time):
    """ Set appointment's begin_time; Pass to apppointment's end date """

    session.attributes['begin_time'] = str(begin_time)
    msg = render_template('end_date')
    return question(msg)

@ask.intent("CMAppointmentEndDateIntent", convert={'end_date': 'date'})
def appointment_end_date(end_date):
    """ Set appointment's end date; Pass to appointment's end time """

    session.attributes['end_date'] = str(end_date)
    msg = render_template('end_time')
    return question(msg)

@ask.intent("CMAppointmentEndTimeIntent", convert={'end_time': 'time'})
def appointment_end_time(end_time):
    """ Set appointment's end time; Create new appointment and rendere result """

    session.attributes['end_time'] = str(end_time)
    form = AppointmentForm(session.attributes)
    form.submit()
    return render_result(form)
