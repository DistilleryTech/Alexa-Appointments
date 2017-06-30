from . import Appointment
from datetime import datetime

class AppointmentForm:

    def __init__(self, attributes):

        formatted_begin_date = '{} {}'.format(
                attributes['begin_date'],
                attributes['begin_time']
        )
        formatted_end_date = '{} {}'.format(
                attributes['end_date'],
                attributes['end_time']
        )
        self.begin_date = datetime.strptime(
                formatted_begin_date, '%Y-%m-%d %H:%M:%S'
        )
        self.end_date = datetime.strptime(
                formatted_end_date, '%Y-%m-%d %H:%M:%S'
        )

    def submit(self):
        self.appointment = Appointment(
                begin_date=self.begin_date,
                end_date=self.end_date
        )
        self.appointment.save()
        return appointment
