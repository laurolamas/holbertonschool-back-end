#!/usr/bin/python3
""" Task 2 """


def write_file(filename="", text=""):
    """ Write file """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)


if __name__ == '__main__':
    import requests
    import sys
    import json

    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users').json()

    output = {}

    for user in users:
        id = user.get('id')

        userTasks = requests.get(
            f'https://jsonplaceholder.typicode.com/users/{id}/todos').json()

        newList = []

        userName = user.get('username')

        for task in userTasks:
            newList.append({
                "username": userName,
                "task": task.get('title'),
                "completed": task.get('completed'),
            })

        output[id] = newList

    write_file("todo_all_employees.json", json.dumps(output))
