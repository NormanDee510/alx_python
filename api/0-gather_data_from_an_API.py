import requests
import sys

def get_employee_info(employee_id):
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

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Print the employee TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
