from flask import Blueprint
from flask_ask import Ask

blueprint = Blueprint('blueprint_api', __name__, url_prefix="/")
ask = Ask(blueprint=blueprint)

from . import launch, new_appointment
