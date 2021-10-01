from flask import Blueprint
app = Blueprint('core', __name__, url_prefix='/')

from . import views
