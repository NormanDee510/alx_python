import csv
import requests
import sys


def check_task_formatting(title):
    """
    Check the formatting of a task title.
    
    Args:
        title (str): The title of the task.

    Returns:
        str: "OK" if the formatting is correct (length >= 10), otherwise "Formatting: Incorrect".
    """
    if len(title) >= 10:
        return "OK"
    else:
        return "Formatting: Incorrect"

def get_employee_info(employee_id):
    """
    Get employee information, TODO list, and export data to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Outputs:
        CSV file: Records all tasks owned by the employee in the format:
                  "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    
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
 
    todos_url = f"{base_url}/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate the number of completed tasks and total tasks
    completed_tasks = [task for task in todos_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)
 
    print(f"Employee {employee_data['name']} is done with tasks({num_completed_tasks}/{total_tasks}):")

    # Print the titles of completed tasks with formatting check
    for i, task in enumerate(completed_tasks, 1):
        formatting_check = check_task_formatting(task['title'])
        print(f"Task {i} Formatting: {formatting_check}")
        print(f"    {task['title']}")

    # Export data to a CSV file
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        
        # Write header row
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write data rows
        for task in todos_data:
            csv_writer.writerow([employee_id, employee_data['username'], task['completed'], task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_info(employee_id)
