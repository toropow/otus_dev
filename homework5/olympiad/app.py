from flask import Flask, render_template
from views import student_app
import os

app = Flask(__name__)

app.register_blueprint(student_app, url_prefix="/student")

images_path = os.path.join('static', 'images')


@app.route('/')
@app.route('/index')
def index():
    img = os.path.join(images_path, 'physics.jpeg')
    return render_template("index.html", img=img)
