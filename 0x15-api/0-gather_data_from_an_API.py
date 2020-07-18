#!/usr/bin/python3
""" Python Script """
import requests
from sys import argv

if __name__ == "__main__":
    u_link = "https://jsonplaceholder.typicode.com/users"
    uid = argv[1]

    u_info = requests.get("{}/{}".format(u_link, uid)).json()
    e_name = u_info['name']

    todo_info = requests.get("{}/{}/todos".format(u_link, uid)).json()
    done = list()
    for todo in todo_info:
        if todo['completed'] is True:
            done.append(todo['title'])
    total = len(todo_info)
    total_done = len(done)

    string = "Employee {} is done with tasks({}/{}):".format(
        e_name, total_done, total)
    print(string)
    for task in done:
        print("\t ", task)
