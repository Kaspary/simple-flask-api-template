from flask import Blueprint
app = Blueprint('core', __name__, url_prefix='/')

from core import views
