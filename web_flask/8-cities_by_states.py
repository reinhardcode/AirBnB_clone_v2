#!/usr/bin/python3
"""flask application to display strates and their cities"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """reload database / teardown"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def with_cities():
    """displays states with cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda d: d.name)
    #for state in states:
        #state.cities = sorted(state.cities, key=lambda d: d.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
