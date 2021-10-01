from flask import Blueprint
app = Blueprint('documentation', __name__, url_prefix='/documentation', template_folder='')

from documentation import views
