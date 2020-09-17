#!/usr/bin/python3
"""
place holder
"""


def number_of_subscribers(subreddit):
    import requests
    req = requests.get("https://api.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "Mozilla/5.0"})
    req = req.json()
    try:
        return req["data"]["subscribers"]
    except Exception as error:
        return 0
