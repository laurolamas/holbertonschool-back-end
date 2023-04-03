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

    for task in emp_tasks:

        output = "\"{}\",\"{}\",\"{}\",\"{}\"".format(
            emp_info.get("id"), emp_info.get("username"),
            task.get("completed"), task.get("tite"))

        with open("USER_ID.csv", mode="a", encoding="utf-8") as f:
            f.write(output)
