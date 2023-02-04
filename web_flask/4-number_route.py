#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def text0_func(text):
    return f'C {text}'


@app.route('/python/<text>')
def text1_func(text):
    return f'Python {text}'

@app.route('/number/<int:n>')
def text2_func(n):
    return f'{n} is a number'


app.run(host='0.0.0.0', port=3000)


