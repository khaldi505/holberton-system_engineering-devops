#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {
            'user-agent': 'my custom user agent 1.0'
    }
    response = requests.get(url, headers=headers)
    data = response.json().get('data')
    if data is None:
        return None
    hot_list += data.get('children', [])
    after = data.get('after', None)
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
