#!/usr/bin/python3
"""Script using API and module requests"""

import csv
import requests
import sys


def export_tasks_to_csv(USER_ID):
    """csv"""

    # Define the API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{USER_ID}/todos"

    # Fetch user information
    user_response = requests.get(user_url)

    user_data = user_response.json()
    USERNAME = user_data['username']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)

    todos_data = todos_response.json()

    # Define CSV file name
    csv_file_name = f"{USER_ID}.csv"

    # Create and write to CSV
    with open(csv_file_name, mode='w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        # Write each TASK_COMPLETED_STATUS to the CSV
        for task in todos_data:
            TASK_COMPLETED_STATUS = task
            TASK_TITLE = task
            csv_writer.writerow([USER_ID, USERNAME,
                                 TASK_COMPLETED_STATUS['completed'],
                                 TASK_TITLE['title']])


if __name__ == "__main__":
    USER_ID = int(sys.argv[1])
    export_tasks_to_csv(USER_ID)
