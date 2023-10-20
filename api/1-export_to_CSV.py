import csv
import requests
from sys import argv

if name == "main":
    if len(argv) < 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    # Fetch employee details
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/%7Bemployee_id%7D")
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employee TODO list
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/users/%7Bemployee_id%7D/todos")
    todos_data = todos_response.json()

    # Create CSV file
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            writer.writerow([employee_id, employee_name, str(task['completed']), task['title']])

    print(f"Data exported to {employee_id}.csv")