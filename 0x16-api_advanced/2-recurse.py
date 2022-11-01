#!/usr/bin/python3
"""returns a list containing the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[]):
    headers = {'User-Agent': 'AgentMEGO'}
    if len(hot_list) == 0:
        resp = requests.get('https://www.reddit.com/r/{}/hot.json'
                            .format(subreddit), headers=headers)
    else:
        resp = requests.get("https://www.reddit.com/r/{}/hot.json?after={}_{}"
                            .format((subreddit), hot_list[-1].get('kind'),
                                    hot_list[-1].get('data').get('id')),
                            headers=headers)
    if resp.status_code != requests.codes.OK:
        return None
    if len(resp.json().get('data').get('children')) < 1:
        return hot_list
    hot_list.extend(resp.json().get('data').get('children'))
    return recurse(subreddit, hot_list)
