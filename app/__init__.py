from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from .widgets import Widget, widgets

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template("index.html",widgets=widgets)
