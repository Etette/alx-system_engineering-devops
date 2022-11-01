#!/usr/bin/python3
"""
Function to queries the REDDIT API
"""
import requests


def number_of_subscribers(subreddit):
    """Prints the titles of the first 10 posts
    listed in /HOT subreddit

    Args:
        subreddit: account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    User_Agent = 'AgentMEGO'
    header = {'User-Agent': User_Agent}
    with requests.Session() as res:
        data = res.get(url, headers=header)
        if data.status_code != 200:
            print(None)
            return
        # return data.json().get('data', {}).get('subscribers', 0)
        data = data.json().get('data').get('children')
        for i in data[0:10]:
            print(i.get('data').get('title'))
