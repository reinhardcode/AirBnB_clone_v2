#!/usr/bin/python3
"""
this module writes a basic flask route
to say hello
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """helo world"""
    return 'Hello HBNB!'


app.run(host='0.0.0.0', port=5000)
