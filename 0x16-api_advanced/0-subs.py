#!/usr/bin/python3
"""
Function to query the REDDIT API
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of total subscribers
    for a given subreddit.
    returns 0 if invalid subreddit is given

    Args:
        subreddit: account to search
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    User_Agent = 'AgentMEGO'
    header = {'User-Agent': User_Agent}
    with requests.Session() as res:
        data = res.get(url, headers=header)
        if data.status_code != 200:
            return 0
    return data.json().get('data', {}).get('subscribers', 0)
