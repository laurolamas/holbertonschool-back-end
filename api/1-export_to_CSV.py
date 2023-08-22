#!/usr/bin/python3
""" Task 1 """


def write_file(filename="", text=""):
    """ Write file """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) != 2:
        print("Enter a valid number")
        sys.exit()

    UserId = sys.argv[1]

    userTasks = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{UserId}/todos').json()
    userInfo = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{UserId}').json()

    userName = userInfo.get('name')
    text = ""
    for task in userTasks:
        text += f"\"{UserId}\",\"{userName}\",\""
        text += f"{task.get('completed')}\",\"{task.get('title')}\"\n"

    write_file(f"{UserId}.csv", text)
