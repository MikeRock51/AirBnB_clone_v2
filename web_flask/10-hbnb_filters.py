#!/usr/bin/python3
"""Starts a python app on 0.0.0.0:5000"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnbFilter():
    """Loads all cities of a state"""
    states = storage.all(States)
    stateCities = {}

    for state in states.values():
        stateCities[state] = state.cities

    return render_template('10-hbnb_filters.html', stateCities=stateCities)


@app.teardown_appcontext
def tearDown(self):
    """Removes the current SQLALchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
