#!/usr/bin/python3
"""
export data in the CSV format.
"""
if __name__ == "__main__":
    import json
    import requests
    file = "todo_all_employees.json"
    u_id = requests.get("https://jsonplaceholder.typicode.com/users").json()
    result = dict()
    for id in u_id:
        result[str(id["id"])] = list()
        username = id["username"]
        tasks = requests.get("https://jsonplaceholder.typicode.com/todos/")
        tasks = tasks.json()
        user_id = id["id"]
        result[str(user_id)] = list()
        for task in tasks:
            result[str(user_id)].append(
                {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }
            )
    with open(file, 'w', newline='') as jsonfile:
        json.dump(result, jsonfile)
