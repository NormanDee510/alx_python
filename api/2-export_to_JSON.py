import requests
import sys
import json

def get_employee_info(employee_id):
    """
    Retrieve employee information and export data in JSON format.

    This function fetches data about an employee from a REST API, including their TODO list.
    It then formats this data according to the specified JSON format and exports it to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Outputs:
        JSON file: Records all tasks owned by the employee in the following format:
                   { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

    Raises:
        ValueError: If the provided employee_id is not a valid integer.
    """
    try:
        employee_id = int(employee_id)
    except ValueError:
        raise ValueError("employee_id must be a valid integer.")

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Make a GET request to get employee details
    employee_url = f"{base_url}/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()

    # Make a GET request to get the employee's TODO list
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Prepare a dictionary to store the tasks in the specified JSON format
    user_tasks = {
        str(employee_id): [
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_data["username"]
            }
            for task in todos_data
        ]
    }

    # Print the JSON data for visual verification
    print(json.dumps(user_tasks, indent=2))

    # Export data to a JSON file
    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(user_tasks, json_file, indent=2)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
