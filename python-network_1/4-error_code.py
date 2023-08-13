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

def search_user_by_letter(letter):
    base_url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    
    response = requests.post(base_url, data=payload)
    
    try:
        response_json = response.json()
        if response_json and 'id' in response_json and 'name' in response_json:
            print(f"[{response_json['id']}] {response_json['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    
    search_user_by_letter(letter)
        