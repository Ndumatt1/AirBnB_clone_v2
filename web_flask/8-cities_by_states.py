#!/usr/bin/python3
''' This module starts a flask web application'''
from flask import Flask
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_list():
    ''' Displays a HTML page'''
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    ''' remove the current SQLALchemy Session'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
