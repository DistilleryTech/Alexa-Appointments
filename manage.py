from flask import Flask
from flask_script import Manager, Server
from models import db
from asks import blueprint
import datetime
import re

app = Flask(__name__)
app.register_blueprint(blueprint)
manager = Manager(app)

@app.template_filter()
def humanize_date(dt):
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])
    month_and_day_of_week = dt.strftime('%A %B')
    day_of_month = ordinal(dt.day)
    year = dt.year if dt.year != datetime.datetime.now().year else ""
    formatted_date = "{} {} {}".format(month_and_day_of_week, day_of_month, year)
    formatted_date = re.sub('\s+', ' ', formatted_date)
    return formatted_date


@app.template_filter()
def humanize_time(dt):
    morning_threshold = 12
    afternoon_threshold = 17
    evening_threshold = 20
    hour_24 = dt.hour
    if hour_24 < morning_threshold:
        period_of_day = "in the morning"
    elif hour_24 < afternoon_threshold:
        period_of_day = "in the afternoon"
    elif hour_24 < evening_threshold:
        period_of_day = "in the evening"
    else:
        period_of_day = " at night"
    the_time = dt.strftime('%I:%M')
    formatted_time = "{} {}".format(the_time, period_of_day)
    return formatted_time


manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

app.config['MONGODB_SETTINGS'] = {
    'db': 'alexa_appointments'
}

db.init_app(app)

if __name__ == '__main__':
    manager.run()
