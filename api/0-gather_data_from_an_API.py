#!/usr/bin/python3
"""
Task 0 fewfewfwef
"""

import requests
import sys


def get_emp_todo_list(emp_id):
    """ Get employer tofo list """

    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}/todos"
    resp = requests.get(url)
    emp_tasks = resp.json()

    url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    resp = requests.get(url)
    emp_info = resp.json()

    emp_name = emp_info.get("name")
    comp_tasks = [task["title"] for task in emp_tasks if task["completed"]]
    num_tasks = len(comp_tasks)
    total_tasks = len(emp_tasks)

    print(f"Employee {emp_name} is done with {num_tasks}/{total_tasks} tasks:")

    for task in comp_tasks:
        print(f"\t {task}")
