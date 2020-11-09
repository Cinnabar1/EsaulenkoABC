from flask.blueprints import Blueprint
from flask import render_template
from Models.Lecturer import Lecturer

lecturers = Blueprint('lecturers', __name__, template_folder='templates', static_folder='static')


@lecturers.route('/lecturers')
def index():
    return render_template('Index.html', lecturers = Lecturer.query.all())
