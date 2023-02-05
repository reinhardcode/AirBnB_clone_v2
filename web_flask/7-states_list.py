#!/usr/bin/python3
"""script that displayes hbnb data"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """close the session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """return all states"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda d: d.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
