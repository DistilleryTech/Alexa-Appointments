from flask import render_template
from flask_ask import question
from . import ask

@ask.launch
def new_session():
    """ Initiates new session; Render 'welcome' response """

    welcome_msg = render_template('welcome')
    return question(welcome_msg)
