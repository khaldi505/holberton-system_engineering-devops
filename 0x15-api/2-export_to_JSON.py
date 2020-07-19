#!/usr/bin/python3
"""
export data in the CSV format.
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv
    u_id = int(argv[1])
    username = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(u_id)).json()
    username = username[0]["username"]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(u_id)).json()
    file = "{}.json".format(u_id)
    result = dict()
    result[str(u_id)] = []
    for task in tasks:
        result[str(u_id)].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            })
    with open(file, 'w', newline='') as jsonfile:
        json.dump(result, jsonfile)
