import requests
import sys


def send_post_request(url, email):
    """
    Send a POST request with an email parameter and display the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include in the POST request.
    """
    email = 'hr@holbertonschool.com'
    data = {'email': email}
    try:
        response = requests.post(url, data=data)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        send_post_request(url, email)
    else:
        print("Usage: python script.py <URL> <email>")
