#!/usr/bin/python3

""" place holder """


def top_ten(subreddit):
    import requests
    link = "https://www.reddit.com/r/{}/top.json?limit=10".format(subreddit)
    result = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
    result = result.json()
    if result["data"]["children"] == []:
        print("None")
    result = result["data"]["children"]
    for x in result:
        print(x["data"]["title"])
