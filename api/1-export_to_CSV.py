import csv
import requests
import sys

def get_employee_info(employee_id):
    """
    Retrieve employee information and TODO list, then export it to a CSV file.

    Args:
        employee_id (int): The ID of the employee for whom to retrieve information.

    Returns:
        None
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

    # Create a CSV file with the specified format
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write TODO list data to the CSV file
        for task in todos_data:
            csv_writer.writerow([employee_id, employee_data['username'], task['completed'], task['title']])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Parse the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to retrieve and export employee data
    get_employee_info(employee_id)
