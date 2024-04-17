#!/usr/bin/python3
"""Script using API and modume requests"""


import requests
import sys


def fetch_todo_progress(employee_id):
    """script API TODO list"""

    employee_id = int(sys.argv[1])
    # Endpoint URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/\
{employee_id}/todos"

    # Fetch user information
    user_response = requests.get(user_url)

    user_data = user_response.json()
    EMPLOYEE_NAME = user_data['name']

    # Fetch TODOs for the user
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate progress
    TOTAL_NUMBER_OF_TASKS = len(todos_data)
    NUMBER_OF_DONE_TASKS = sum(1 for TASK_TITLE in
                               todos_data if TASK_TITLE['completed'])

    # Print progress
    print(f"Employee {EMPLOYEE_NAME} is done with tasks\
({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    for TASK_TITLE in todos_data:
        if TASK_TITLE['completed']:
            print(f"\t {TASK_TITLE['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
