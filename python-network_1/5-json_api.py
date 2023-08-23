"""
Send a POST request to search user by letter and display response information.

This script takes a letter as input, sends a POST request to a URL with the letter as
a parameter, and displays user information from the response if the JSON is properly
formatted and not empty.

Usage:
    python script.py <letter>

Args:
    letter (str): The letter to search for.

Example:
    python script.py a
"""

import requests
import sys

def search_user_by_letter(letter):
    """
    Send a POST request to search user by letter and display response information.

    Args:
        letter (str): The letter to search for.
    """
    url = "http://0.0.0.0:5000/search_user"
    letter = "h"
    data = {'q': letter}
    
    try:
        response = requests.post(url, data=data)
        response_json = response.json()
        
        if isinstance(response_json, list) and response_json:
            user = response_json[0]
            print(f"[{user['id']}] {user['name']}")
        elif not response_json:
            print("No result")
        else:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
        search_user_by_letter(letter)
    else:
        print("No result")
