#!/usr/bin/python3
""" Task 0 """

import requests
import sys

emp_id = sys.argv[1]

url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
resp = requests.get(url)
emp_tasks = resp.json()

url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
resp = requests.get(url)
emp_info = resp.json()


emp_name = emp_info.get("name")
completed_tasks = [task["title"] for task in emp_tasks if task["completed"]]
num_tasks = len(completed_tasks)
total_tasks = len(emp_tasks)

print(f"Employee {emp_name} is done with {num_tasks}/{total_tasks} tasks:")

for task in completed_tasks:
    print(f"\t {task}")
