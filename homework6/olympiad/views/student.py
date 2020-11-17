from flask import Blueprint, render_template, request
from models import db, Student

student_app = Blueprint("student_app", __name__)


def add_participants(firstname: str, lastname: str) -> None:
    student = Student(first_name=firstname, last_name=lastname)
    db.session.add(student)
    db.session.commit()


def get_all_participants() -> Student:
    return Student.query.order_by(Student.id).all()


@student_app.route('/participants')
def participants():
    students = get_all_participants()
    return render_template("participants.html", participants=students)


@student_app.route('/registration', methods=["POST"])
def create_participants():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    add_participants(firstname=firstname, lastname=lastname)
    students = get_all_participants()
    return render_template("participants.html", participants=students)


@student_app.route('/registration',  methods=["GET"])
def reg_form():
    return render_template("registration.html")
