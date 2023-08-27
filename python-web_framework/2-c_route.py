"""
This is a simple Flask web application.
It listens on 0.0.0.0, port 5000 and provides basic routes.
"""

from flask import Flask

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


@app.errorhandler(404)
def page_not_found(error):
    """
    Error handler for 404 (Not Found) errors.
    Returns a custom message for invalid routes.
    """
    return "404 Not Found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)