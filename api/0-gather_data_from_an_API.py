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


def fetch_api_data(url, params=None):
    """Helper function to fetch data from the API.

    Sends a GET request to the specified URL with optional query parameters.
    If the request is successful, returns the JSON response data. Otherwise,
    prints an error message and returns None.

    Args:
        url (str): The URL to send the GET request to.
        params (dict): Optional query parameters for the request.

    Returns:
        dict: The JSON response data, or None if there was an error.
    """
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Failed to fetch data from {url}. HTTP status code: "
            f"{response.status_code}"
        )
        return None


def get_employee_name(employee_id):
    """Fetches and returns the name of an employee given their employee ID.

    Arguments:
        employee_id (int): The ID of the employee.

    Returns:
        str: The name of the employee, or None if there was an error.
    """
    # Base URL for the REST API
    base_url = "https://jsonplaceholder.typicode.com/users/"

    # Fetch data using the helper function
    employee_info = fetch_api_data(f"{base_url}{employee_id}")

    # Return the employee's name
    return employee_info.get('name') if employee_info else None


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
    params = {'userId': employee_id}

    # Fetch data using the helper function
    todos = fetch_api_data(base_url, params=params)

    if todos is None:
        return None, None, None

    # Initialize counters
    completed_todos = 0
    total_todos = 0
    completed_task_titles = []

    # Iterate through the list of todos
    for todo in todos:
        is_completed = todo.get('completed', False)
        title = todo.get('title', '')

        total_todos += 1
        if is_completed:
            completed_todos += 1
            completed_task_titles.append(title)

    # Return the results
    return completed_todos, total_todos, completed_task_titles


def main():
    """Main function that executes when the script is run directly."""
    # Check if an employee ID is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Parse the employee ID from command line argument
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Invalid employee ID. Please provide an integer.")
        sys.exit(1)

    # Get the employee's name
    employee_name = get_employee_name(employee_id)
    if employee_name is None:
        print(f"Employee ID {employee_id} not found.")
        sys.exit(1)

    # Get the employee's TODO progress
    completed_todos, total_todos, completed_task_titles = (
        get_todo_progress(employee_id)
    )
    if completed_todos is None or total_todos is None:
        sys.exit(1)

    # Print the progress summary
    print(f"Employee {employee_name} is done with tasks"
          f"({completed_todos}/{total_todos}):")

    # Print titles of completed tasks
    for title in completed_task_titles:
        print("\t" + title)


if __name__ == "__main__":
    main()
