import requests
import sys
tasks = 0
done = 0
titles = ""
username = ""
users = requests.get("https://jsonplaceholder.typicode.com/users")
users = users.json()
for x in range(len(users)):
    if(int(sys.argv[1]) == users[x]["id"]):
        username = users[x]["name"]
        break
users = requests.get("https://jsonplaceholder.typicode.com/todos")
users = users.json()
for y in range(len(users)):
    if (int(sys.argv[1]) == users[y]["userId"]):
        tasks += 1
        if (users[y]["completed"]):
            done += 1
            titles += "\t" + " " + users[y]["title"] + '\n'

parg = "Employee {} is done with tasks({}/{})".format(username, done, tasks)
print(parg)
print("{}".format(titles), end='')
