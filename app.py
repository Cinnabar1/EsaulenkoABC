from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.Interval import Interval
from Models.Group import Group
from Models.Schedule import Schedule
from Models.Lecturer import Lecturer
from Models.Subject import Subject

from Routes.Lecturers import lecturers
from Routes.Intervals import intervals

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lecturers)
app.register_blueprint(intervals)
if __name__ == '__main__':
    app.run()

