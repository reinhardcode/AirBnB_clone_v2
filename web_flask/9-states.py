#!/usr/bin/python3
"""this module does the states and state diffrently"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """reload database / teardown"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<string:id>", strict_slashes=False)
def states(id=""):
    """Return all states formatted in HTML"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda d: d.name)
    if id != "":
        state = None
        for d in states:
            if d.id == id:
                state = d
                break
        if state is not None:
            state.cities = sorted(state.cities, key=lambda d: d.name)
        return render_template("9-states.html", state=state)
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
