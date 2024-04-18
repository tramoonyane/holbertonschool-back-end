#!/usr/bin/python3
"""Script using API and module requests to export data in CSV format."""

import csv
import requests
import sys


def fetch_todo_progress_and_export_to_csv(employee_id):
    """Fetch TODO list data and export it to a CSV file."""
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    user_data = user_response.json()
    USERNAME = user_data['username']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Define CSV file name
    csv_filename = f"{employee_id}.csv"

    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write data to CSV file
        for task in todos_data:
            TASK_COMPLETED_STATUS = str(task['completed'])  # Convert to string
            TASK_TITLE = task['title']
            csv_writer.writerow([employee_id, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])

    print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_progress_and_export_to_csv(employee_id)
