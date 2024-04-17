#!/usr/bin/python3

"""Module for fetching employee TODO list progress from a REST API.

This module contains functions to retrieve information about an employee's
TODO list progress and print it in a specified format. It uses the
jsonplaceholder.typicode.com API to fetch data about employees and their
TODO lists.

Functions:
    get_employee_name(employee_id): Fetches and returns the name of an
        employee given their employee ID.
    get_todo_progress(employee_id): Fetches and returns the progress of an
        employee's TODO list, including the count of completed and total
        tasks and the titles of completed tasks.
    main(): Executes the script's main functionality if the script is run
        directly from the command line.
"""

import sys
import requests


def get_employee_name(employee_id):
    """Fetches and returns the name of an employee given their employee ID.

    Arguments:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee, or None if there was an error.
    """
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com/users/"

    # Send a GET request to the endpoint with the employee ID
    response = requests.get(f"{base_url}{employee_id}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data to get employee info
        employee_info = response.json()
        # Return the employee's name
        return employee_info.get('name')
    else:
        # Handle the error
        print(f"Failed to fetch employee data for ID {employee_id}.")
        print(f"HTTP status code: {response.status_code}")
        return None


def get_todo_progress(employee_id):
    """Fetches and returns an employee's TODO list progress.

    Given an employee ID, this function retrieves the employee's TODO list
    from the REST API and calculates the number of completed tasks and the
    total number of tasks. It also returns a list of titles for the completed
    tasks.

    Arguments:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing:
            - int: Number of completed tasks.
            - int: Total number of tasks.
            - list of str: Titles for the completed tasks.

    If there is an issue fetching the TODO list data, returns
    a tuple of (None, None, None).
    """
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com/todos"
    # Specify the query parameters for the given employee ID
    params = {'userId': employee_id}

    # Send a GET request to the endpoint
    response = requests.get(base_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        todos = response.json()

        # Initialize counters
        completed_todos = 0
        total_todos = 0

        # List of titles for completed tasks
        completed_task_titles = []

        # Iterate through the list of todos
        for todo in todos:
            # Get the completed status and title
            is_completed = todo.get('completed', False)
            title = todo.get('title', '')

            total_todos += 1
            if is_completed:
                completed_todos += 1
                completed_task_titles.append(title)

        # Return the results
        return completed_todos, total_todos, completed_task_titles
    else:
        # Handle the error
        print(f"Failed to fetch TODO data for employee ID {employee_id}.")
        print(f"HTTP status code: {response.status_code}")
        return None, None, None


def main():
    # Check for employee ID provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse the employee ID
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Provide an integer.")
        sys.exit(1)

    # Get employee's name
    employee_name = get_employee_name(employee_id)
    if employee_name is None:
        sys.exit(1)

    # Get TODO progress
    completed_todos, total_todos, completed_task_titles = get_todo_progress(
        employee_id
    )
    if completed_todos is None or total_todos is None:
        sys.exit(1)

    # Print the progress
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_todos}/{total_todos}):")

    # Print titles of completed tasks
    for title in completed_task_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
