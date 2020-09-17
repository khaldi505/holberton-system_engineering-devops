#!/usr/bin/python3

""" place holder """


def top_ten(subreddit):
    import requests
    from sys import argv
    link = "https://www.reddit.com/r/{}/top.json?limit=10".format(argv[1])
    result = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
    result = result.json()
    if result["data"]["children"] == []:
        print("None")
    result = result["data"]["children"]
    for x in result:
        print(x["data"]["title"])
