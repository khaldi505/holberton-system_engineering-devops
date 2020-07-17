#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her
TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()
    tasks = 0
    done = 0
    titles = ""
    username = ""
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1]))
    if users.status_code == 200:
        users = users.json()
        username = users["name"]
        users = requests.get("https://jsonplaceholder.typicode.com/todos")
        if users.status_code != 200:
            exit()
        users = users.json()
        for y in range(len(users)):
            if (int(sys.argv[1]) == users[y]["userId"]):
                tasks += 1
                if (users[y]["completed"]):
                    done += 1
                    titles += "\t" + " " + users[y]["title"] + '\n'

        parg = "Employee {} is done with tasks({}/{})".format(
            username, done, tasks)
        print(parg)
        print("{}".format(titles), end='')
