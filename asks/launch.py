from flask import render_template
from flask_ask import question
from . import ask

@ask.launch
def new_session():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)
