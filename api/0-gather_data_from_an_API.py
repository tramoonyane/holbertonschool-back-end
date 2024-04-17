#!/usr/bin/python3
"""
Script to fetch and display the progress of an employee's to-do list
from the JSONPlaceholder API.
"""

import requests
import sys


def fetch_user_data(employee_id):
    """Fetch and display the progress of an employee's to-do list."""
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch the user information
    user = requests.get(f"{url}users/{employee_id}").json()

    if not user:
        print(f"Employee with ID {employee_id} not found.")
        return

    # Fetch the to-do list for the user
    todo_list = requests.get(f"{url}todos?userId={employee_id}").json()

    # Calculate the number of completed tasks and the total number of tasks
    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)
    completed_count = len(completed_tasks)

    # Display the employee name and the to-do list progress
    print(f"Employee {user['name']} is done with tasks({completed_count}/{total_tasks}):")

    # Display the title of completed tasks
    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    # Check if an argument was provided
    if len(sys.argv) < 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from the command-line argument
    employee_id = int(sys.argv[1])

    # Call the function to fetch user data
    fetch_user_data(employee_id)
