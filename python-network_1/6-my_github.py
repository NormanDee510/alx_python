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

def get_github_user_id(username, access_token):
    """
    Use GitHub API with Basic Authentication to display user id.

    Args:
        username (str): Your GitHub username.
        access_token (str): Your GitHub personal access token.
    """
    url = f"https://api.github.com/NormanDee510"
    headers = {"Authorization": f"Basic {access_token}"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        else:
            print("None")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        personal_access_token = sys.argv[2]
        get_github_user_id(username, personal_access_token)
    else:
        print("Usage: python script.py NormanDee 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")