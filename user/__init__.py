from flask import Blueprint
app = Blueprint('user', __name__, url_prefix='/user')

from . import views, commands
