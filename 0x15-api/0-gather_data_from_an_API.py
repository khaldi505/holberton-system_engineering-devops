#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her
TODO list progress.
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    u_id = argv[1]
    user_name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(u_id)
        ).json()
    user_name = user_name[0]["name"]
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}".format(u_id)
        ).json()
    x = 0
    todo_titles = []
    done = 0
    for todo in todos:
        if todo["completed"]:
            done += 1
            todo_titles.append(todo["title"])
    print(
        "Employee {:s} is done with tasks({:d}/{:d}):"
        .format(user_name, done, len(todos))
        )
    for x in todo_titles:
        print(" \t{:s}".format(x))
