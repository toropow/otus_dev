from flask import Blueprint, render_template, request

student_app = Blueprint("student_app", __name__)

PARTICIPANTS = [
    {'firstname': 'Boris', 'lastname': 'Ivanov'},
    {'firstname': 'Ivan', 'lastname': 'Petrov'},
]


@student_app.route('/participants')
def participants():
    return render_template("participants.html", participants=PARTICIPANTS)


@student_app.route('/registration', methods=["POST"])
def create_participants():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    PARTICIPANTS.append({'firstname': firstname, 'lastname': lastname})
    return render_template("participants.html", participants=PARTICIPANTS)


@student_app.route('/registration',  methods=["GET"])
def reg_form():
    return render_template("registration.html")
