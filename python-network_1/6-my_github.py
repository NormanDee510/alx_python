"""
Use GitHub API with Basic Authentication to display user id.

This script takes GitHub credentials (username and personal access token) as input,
uses Basic Authentication with the personal access token, and displays the user id.

Usage:
    python script.py <username> <personal_access_token>

Args:
    username (str): Your GitHub username.
    personal_access_token (str): Your GitHub personal access token.

Example:
    python script.py papamuziko cisfun
"""

import requests
import sys

def main():
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)
    else:
        print("None")

if __name__ == "__main__":
    main()