import requests
import sys
import json

def get_employee_info(employee_id):
    """
    Retrieve employee information and their TODO list.

    Args:
        employee_id (int): The ID of the employee for whom to retrieve data.

    Returns:
        dict: A dictionary containing the employee's tasks in the specified format.
    """

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
                "username": employee_data["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos_data
        ]
    }

    return user_tasks

def export_all_employees_data():
    """
    Export data for all employees in the specified JSON format and save it to a JSON file.
    """

    all_employees_data = {}
    # Assuming employee IDs range from 1 to 10 (adjust as needed)
    for employee_id in range(1, 11):
        user_tasks = get_employee_info(employee_id)
        all_employees_data.update(user_tasks)

    # Export data to a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=2)

    print(f"Data exported to {json_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python gather_data_from_an_API.py")
        sys.exit(1)

    export_all_employees_data()
