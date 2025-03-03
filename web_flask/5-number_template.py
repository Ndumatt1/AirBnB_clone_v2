#!/usr/bin/python3
''' This module starts a flask web application'''
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    ''' Display Hello HBNB '''
    return "Hello HBNB"


@app.route("/hbnb")
def hbnb():
    ''' Display HBNB'''
    return "HBNB"


@app.route("/c/<text>")
def display_c(text):
    ''' Display C followed by the value of the text variable'''
    new_text = text.replace("_", " ")
    return "C {}".format(new_text)


@app.route("/python/")
@app.route("/python/<text>/")
def display_python(text="is cool"):
    ''' Display Python followed by the value of the text variable '''
    new_text = text.replace("_", " ")
    return "Python {}".format(new_text)


@app.route("/number/<int:n>")
def number(n):
    ''' Display n is a number only if n is an integer '''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
