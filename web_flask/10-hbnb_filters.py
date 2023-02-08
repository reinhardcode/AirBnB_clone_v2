#!/usr/bin/python3
"""
this module creates a flask apllication
for the airbnb project which impiments a filter
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """reload database / teardown"""
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb():
    """this is the function for this route"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    states = sorted(states, key=lambda d: d.name)
    amenities = sorted(amenities, key=lambda d: d.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda d: d.name)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)