#!/usr/bin/python3
''' This module starts a flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    ''' Displays Hello HBNB!'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' Displays HBNB'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    ''' Display C followed by the value of text '''
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
