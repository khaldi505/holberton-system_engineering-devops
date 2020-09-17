#!/usr/bin/python3

""" place holder """


def top_ten(subreddit):
    import requests
    link = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    result = requests.get(link, headers={"User-Agent": "Mozilla/5.0"})
    result = result.json()
    try:
        result = result["data"]["children"][:10]
        for x in result:
            print("{}".format(x["data"]["title"]))
    except Exception as error:
        print("None")
