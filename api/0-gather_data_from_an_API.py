#!/usr/bin/python3
"""
Task 0 fewfewfwef
"""


if __name__ == '__main__':
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
    comp_tasks = [task["title"] for task in emp_tasks if task["completed"]]
    num_tasks = len(comp_tasks)
    total_tasks = len(emp_tasks)

    print(f"Employee {emp_name} is done with {num_tasks}/{total_tasks} tasks:")

    for task in comp_tasks:
        print(f"\t {task}")
