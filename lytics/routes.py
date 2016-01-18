from flask import current_app, Blueprint, render_template
from lytics.db.models import Expenditure
from lytics.db.queries import QueryConn
main = Blueprint('main', __name__, url_prefix='/')

@main.route("/")
def index():
        return render_template('index.jinja2')
