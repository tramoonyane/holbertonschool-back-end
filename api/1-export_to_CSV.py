#!/usr/bin/python3

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Retrieves and prints the TODO list progress of an employee based on the given employee ID.

    The function fetches data from the JSONPlaceholder REST API to find the employee's name and TODO list.
    It then calculates the number of completed tasks and total tasks, and prints the information in the
    required format.

    :param employee_id: An integer representing the employee ID.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = f'{base_url}users/{employee_id}'
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Error: Could not retrieve information for employee ID {employee_id}")
        return
    user_data = user_response.json()
    employee_name = user_data.get('name')
    employee_username = user_data.get('username')
    if employee_name is None:
        print(f"Error: Employee ID {employee_id} does not exist.")
        return
    todos_url = f'{base_url}todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"Error: Could not retrieve TODO list for employee ID {employee_id}")
        return
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    done_tasks = [todo for todo in todos_data if todo.get('completed')]
    number_of_done_tasks = len(done_tasks)
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
    filename = f'{employee_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todos_data:
            user_id = employee_id
            task_completed_status = task.get('completed')
            task_title = task.get('title')
            csv_writer.writerow([user_id, employee_username, task_completed_status, task_title])
    print(f"Data exported to {filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    get_employee_todo_progress(employee_id)
