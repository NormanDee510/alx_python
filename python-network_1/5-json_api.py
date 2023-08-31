import sys
import requests


def search_user_by_letter(letter):
    """
    Send a POST request to search user by letter and display response information.

    Args:
        letter (str): The letter to search for.
    """
    url = "http://0.0.0.0:5000/search_user"
    
    
    data = {'q': letter}
    
    try:
        response = requests.post(url, data=data)
        try:
            response_json = response.json()
        except ValueError:
            response_json = None
        
        if isinstance(response_json, list) and response_json:
            user = response_json[0]
            print(f"[{user['id']}] {user['name']}")
        elif not response_json:
            print("Not a valid JSON")
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
