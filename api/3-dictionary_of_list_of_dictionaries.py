#!/usr/bin/python3

import json
import requests

def fetch_todo_data():
    """
    Fetches and exports tasks data for all employees from the JSONPlaceholder REST API.

    The function collects tasks data for all employees and exports it to a JSON file named
    `todo_all_employees.json` in the required format.

    The JSON format is:
    {
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            ...
        ],
        "USER_ID": [
            {
                "username": "USERNAME",
                "task": "TASK_TITLE",
                "completed": TASK_COMPLETED_STATUS
            },
            ...
        ],
        ...
    }
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    
    
    users_url = f'{base_url}users'
    users_response = requests.get(users_url)
    
    if users_response.status_code != 200:
        print("Error: Could not retrieve users data.")
        return
    
    users_data = users_response.json()
    
    
    tasks_dict = {}
    
    
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')
        
       
        todos_url = f'{base_url}todos?userId={user_id}'
        todos_response = requests.get(todos_url)
        
        if todos_response.status_code != 200:
            print(f"Error: Could not retrieve TODO list for user ID {user_id}")
            continue
        
        todos_data = todos_response.json()
        
        
        user_tasks = []
        
        
        for task in todos_data:
            task_dict = {
                "username": username,
                "task": task.get('title'),
                "completed": task.get('completed')
            }
            user_tasks.append(task_dict)
        
        
        tasks_dict[user_id] = user_tasks
    
    
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as jsonfile:
        json.dump(tasks_dict, jsonfile)
    
    print(f"Data exported to {filename}")

if __name__ == '__main__':
    fetch_todo_data()
