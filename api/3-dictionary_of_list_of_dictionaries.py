#!/usr/bin/python3
"""
Task 0 fewfewfwef
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    url = f"https://jsonplaceholder.typicode.com/users/"
    resp = requests.get(url)
    users = resp.json()

    all_todos = {}

    for user in users:

        user_id = user.get("id")
        emp_todos = []

        url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
        resp = requests.get(url)
        todos = resp.json()

        for task in todos:
            emp_todos.append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': user.get('username')})

        all_todos[user_id] = emp_todos

        with open("todo_all_employees.json", mode="w", encoding="utf-8") as f:
            json.dump(all_todos, f)
