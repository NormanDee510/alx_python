"""
Send a request to a URL, display response body, and handle error codes.

This script takes a URL as input, sends a request to the URL, displays the body of
the response, and prints an error code if the HTTP status code is greater than or
equal to 400.

Usage:
    python script.py <URL>

Args:
    URL (str): The URL to send the request to.

Example:
    python script.py http://0.0.0.0:5000
"""

import requests
import sys

def fetch_and_display_response(url):
    """
    Send a request to a URL, display response body, and handle error codes.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        fetch_and_display_response(url)
    else:
        print("Usage: python script.py <URL>")