#!/usr/bin/python3
''' THis module starts a flask web application '''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashed = False


@app.route("/")
def hello():
    ''' Displays Hello HBNB!'''
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    ''' Displays HBNB'''
    return "HBNB"


@app.route("/c/<text>")
def display_c(text):
    ''' Display C followed by the value of the text variable '''
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python/")
@app.route("/python/<text>")
def display_python(text):
    ''' Displays Python followed by the value of the text variable'''
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<int:n>")
def display_number(n):
    ''' Display n is a number only if n is an integer'''
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
