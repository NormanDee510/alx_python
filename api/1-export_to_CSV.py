#Gather Data From an API

import csv
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    # Request employee details and todo list from the API
    response_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    response_todos = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if response_user.status_code == 200 and response_todos.status_code == 200:
        user_data = json.loads(response_user.text)
        todos_data = json.loads(response_todos.text)

        employee_name = user_data.get("name")
        user_id = user_data.get("id")
        total_tasks = len(todos_data)
        completed_tasks = []

        for task in todos_data:
            if task["completed"]:
                completed_tasks.append(task["title"])

        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t{task}")

        # Export data to a CSV file
        csv_filename = f"{user_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
            for task in todos_data:
                task_status = "Completed" if task["completed"] else "Incomplete"
                csv_writer.writerow([user_id, employee_name, task_status, task["title"]])

        print(f"Data exported to {csv_filename}")
    else:
        print("Failed to retrieve data. Please check the employee ID and API availability.")