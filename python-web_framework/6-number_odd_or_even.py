"""
This is a simple Flask web application.
It listens on 0.0.0.0, port 5000 and provides basic routes.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL.
    Returns a greeting message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the /hbnb URL.
    Returns a message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the /c/<text> URL.
    Returns "C " followed by the value of the text variable.
    Underscore _ symbols are replaced with spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
    Route handler for the /python/ URL and /python/<text> URL.
    Returns "Python " followed by the value of the text variable.
    If no text is provided, "is cool" is used as the default.
    Underscore _ symbols are replaced with spaces.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route handler for the /number/<n> URL.
    Displays "n is a number" if n is an integer.
    """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route handler for the /number_template/<n> URL.
    Displays an HTML page with the number n.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route handler for the /number_odd_or_even/<n> URL.
    Displays an HTML page indicating whether the number n is even or odd.
    """
    odd_or_even = "odd" if n % 2 != 0 else "even"
    return render_template(
        '6-number_odd_or_even.html', n=n, odd_or_even=odd_or_even
        )


@app.errorhandler(404)
def page_not_found(error):
    """
    Error handler for 404 (Not Found) errors.
    Returns a custom message for invalid routes.
    """
    return "404 Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
