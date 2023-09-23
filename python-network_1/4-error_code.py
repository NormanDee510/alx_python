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


def main():
    url = sys.argv[1]
    
    response = requests.get(url)
    responsebody = response.text
    
    if response.status_code > 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(responsebody)
if __name__=="__main__":
    main()

        