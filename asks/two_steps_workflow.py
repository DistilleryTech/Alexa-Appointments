from . import (ask, session, render_template, question, statement,
               Appointment, AppointmentForm, render_result)

@ask.intent("CMAppointmentWithBeginDateAndTimeIntent",
            convert={'begin_date': 'date', 'begin_time': 'time'})
def appointment_with_begin_date(begin_date, begin_time):
    """
    Set appointment's begin date and time;
    Pass to definition of end date and time
    """

    session.attributes['begin_date'] = str(begin_date)
    session.attributes['begin_time'] = str(begin_time)
    msg = render_template('end_date')
    return question(msg)

@ask.intent("CMAppointmentWithEndDateAndTimeIntent",
            convert={'end_date': 'date', 'end_time': 'time'})
def appointment_with_end_date(end_date, end_time):
    """
    Set appointment's end date and time;
    Create new appointment and render result message
    """

    session.attributes['end_date'] = str(end_date)
    session.attributes['end_time'] = str(end_time)
    form = AppointmentForm(session.attributes)
    form.submit()
    render_result(form)
