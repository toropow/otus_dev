from flask import Flask, render_template
from views import student_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os
import config
from models import db

app = Flask(__name__)

app.config.update(SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
                  SQLALCHEMY_TRACK_MODIFICATIONS=False)


migrate = Migrate(app, db)
app.register_blueprint(student_app, url_prefix="/student")
db.init_app(app)
images_path = os.path.join('static', 'images')


@app.route('/')
@app.route('/index')
def index():
    img = os.path.join(images_path, 'physics.jpeg')
    return render_template("index.html", img=img)
