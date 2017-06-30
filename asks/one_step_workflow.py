from . import (ask, session, render_template, question, statement,
               Appointment, AppointmentForm)

@ask.intent("CMAppointmentWithFullDataIntent",
            convert={'begin_date': 'date', 'begin_time': 'time',
                     'end_date': 'date', 'end_time': 'time'})
def appointment_with_full_date(begin_date, begin_time, end_date, end_time):
    """
    Set all the necessary for appointment attributes;
    Create new appointment and render result
    """
    
    session.attributes['begin_date'] = str(begin_date)
    session.attributes['begin_time'] = str(begin_time)
    session.attributes['end_date'] = str(end_date)
    session.attributes['end_time'] = str(end_time)
    form = AppointmentForm(session.attributes)
    form.submit()
    render_result(form)

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
    """
        Override default Amazon intent.
        WORK IN PROGRESS
        TODO:
            - add more conditions with asks about missing data
            - rendere result message based on given information
    """

    if object_start_date is None:
        return question('date')
    if object_start_time is None:
        return question('time')
