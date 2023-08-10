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
    python script.py http://localhost:5000/api/endpoint user@example.com
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
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)
    else:
        print("Usage: python script.py <URL> <email>")