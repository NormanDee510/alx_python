import requests
import sys

def get_x_request_id(url):
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
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        get_x_request_id(url)
    else:
        print("Usage: python script.py <URL>")