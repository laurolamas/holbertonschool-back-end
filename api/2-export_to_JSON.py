#!/usr/bin/python3
"""
Task 0 fewfewfwef
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    emp_id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    resp = requests.get(url)
    emp_info = resp.json()

    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    resp = requests.get(url)
    emp_tasks = resp.json()

    emp_todos = []

    for task in emp_tasks:
        emp_todos.append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': emp_info.get('username')})

    output_json = {str(emp_id): emp_todos}

    with open(f"{emp_id}.json", mode="a", encoding="utf-8") as f:
        json.dump(output_json, f)
