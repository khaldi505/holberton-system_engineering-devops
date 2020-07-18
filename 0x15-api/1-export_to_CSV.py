#!/usr/bin/python3
"""
export data in the CSV format.
"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv
    u_id = int(argv[1])
    user_name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(u_id)
    ).json()
    user_name = user_name[0]["username"]
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}".format(u_id)
    ).json()
    todo_titles = []
    completed = []
    for todo in todos:
        todo_titles.append(todo["title"])
        completed.append(todo["completed"])
    x = 0
    with open('{}.csv'.format(u_id), mode='w') as csv_file:
        wirter = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for x in range(len(completed)):
            wirter.writerow([u_id, user_name, completed[x], todo_titles[x]])
