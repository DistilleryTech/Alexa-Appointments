from flask import Flask
from flask_script import Manager, Server
from models import db
from asks import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)
manager = Manager(app)

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
