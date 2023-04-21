#!/usr/bin/python3
"""Starts a Flask application on 0.0.0.0:5000"""


from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a simple greeting page"""

    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a page containing the string 'HBNB'"""

    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def dear_c(text):
    """Returns a page about C"""

    text = text.split('_')
    text = " ".join(text)

    return ("C {}".format(text))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def dear_python(text="is cool"):
    """Returns a page about Python"""

    if text != 'is cool':
        text = text.split('_')
        text = " ".join(text)
    return ("Python {}".format(text))


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """Checks if input is a number"""

    if n.isdigit():
        return ("{} is a number".format(n))
    else:
        abort(404)


@app.route('/number_template/<n>')
def is_number_template(n):
    if n.isdigit():
        return (render_template('5-number.html', n=n))
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
