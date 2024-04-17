#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.

Usage:
    ./script.py <employee_id>
    <employee_id> should be an integer representing the employee ID.
"""

import sys
import requests


def main():
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Check if the employee ID argument is provided
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        return

    try:
        # Convert employee ID argument to an integer
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: employee_id must be an integer.")
        return

    # Get the employee information using the provided employee ID
    response_user = requests.get(url + "users/{}".format(employee_id))

    # Check for a valid response
    if response_user.status_code != 200:
        print("Error: Could not fetch employee data. Check the employee ID.")
        return

    # Parse the user data
    user = response_user.json()
    employee_name = user.get("name")

    # Get the to-do list for the employee using the provided employee ID
    response_todos = requests.get(
        url + "todos", params={"userId": employee_id}
    )

    # Check for a valid response
    if response_todos.status_code != 200:
        print("Error: Could not fetch todo list. Check the employee ID.")
        return

    # Parse the todo list data
    todos = response_todos.json()

    # Filter completed tasks and count them
    completed_tasks = [task for task in todos if task.get("completed")]

    # Print the employee's name and the number of completed tasks
    print(f"Employee {employee_name} is done with tasks"
          f"({len(completed_tasks)}/{len(todos)}):")

    # Print the completed tasks one by one with indentation
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()
