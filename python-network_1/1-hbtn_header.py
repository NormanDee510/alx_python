#!/usr/bin/env python3
"""
Send a GET request to a URL and display the value of X-Request-Id in the response header.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        
        if x_request_id:
            print(x_request_id)
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
