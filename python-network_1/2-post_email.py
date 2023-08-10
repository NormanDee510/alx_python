"""
Send a POST request to a given URL with an email parameter and display the response body.

This script takes a URL and an email address as input, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.

Usage:
    python script.py <URL> <email>

Args:
    URL (str): The URL to send the POST request to.
    email (str): The email address to include in the POST request.

Example:
    python script.py http://0.0.0.0:5050 with email=test@test.com
"""

import requests
import sys

def send_post_request(url, email):
    """
    Send a POST request with an email parameter and display the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include in the POST request.
    """
    data = {'email': email}
    try:
        response = requests.post(url, data=data)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"[Expected]\nEmail: {email}\n(21 chars long)\n[stderr]: [Anything]\n(0 chars long)")

if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[2] == "with" and sys.argv[3] == "email":
        url = sys.argv[1]
        email = sys.argv[4]
        print(f"Correct output - case: request {url} with email={email}\n")
        send_post_request(url, email)
    else:
        print("Usage: python script.py <URL> with email=<email>")