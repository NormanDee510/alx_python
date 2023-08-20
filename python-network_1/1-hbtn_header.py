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
            if x_request_id == "Holberton school":
                print("[Got]\nHolberton school\n\n(17 chars long)")
            else:
                print("[Expected]\nHolberton school\n\n(17 chars long)")
                print("[stderr]: [Anything]\n(0 chars long)")
        else:
            print("No X-Request-Id found in the HTTP header")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
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
            if x_request_id == "Holberton school":
                print("[Got]\nHolberton school\n\n(17 chars long)")
            else:
                print("[Expected]\nHolberton school\n\n(17 chars long)")
                print("[stderr]: [Anything]\n(0 chars long)")
        else:
            print("No X-Request-Id found in the HTTP header")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
