#!/usr/bin/python3
"""
place holder
"""


if __name__ == "__main__":
    import requests
    import json
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos")
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users")
    todos = todos.json()
    users = users.json()
    result = {}
    for user in users:
        result[user["id"]] = []
        for todo in todos:
            result[user["id"]].append(
                {"username": user["username"],
                    "task": todo["title"], "completed": todo["completed"]})
    with open("todo_all_employees.json", 'w') as result_file:
        json.dump(result, result_file)
