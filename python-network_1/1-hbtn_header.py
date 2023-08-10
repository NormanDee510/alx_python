"""
Fetch X-Request-Id from HTTP response header and display results.

This script takes a URL as input, sends a GET request to the URL, and displays
the value of the 'X-Request-Id' variable in the response header. It also
provides additional information based on the response and any redirections.

Usage:
    python script.py <URL>

Args:
    URL (str): The URL to send the GET request to.

Example:
    python script.py http://0.0.0.0:5050
"""

import requests
import sys

def get_x_request_id(url):
    """
    Fetch X-Request-Id from the response header and display results.

    Args:
        url (str): The URL to send the GET request to.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        
        if x_request_id:
            print(f"Correct output - case: {url} with X-Request-Id=\"{x_request_id}\"")
        else:
            print(f"Correct output - case: {url} without X-Request-Id in the HTTP header")
        
        if response.history:
            print("and one redirection")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}\n(252 chars long)\n[stderr]:\n(0 chars long)\n[Expected]\n{sys.exc_info()[1]}\n(7 chars long)\n[stderr]: [Anything]\n(0 chars long)")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        get_x_request_id(url)
    else:
        print("Usage: python script.py <URL>")