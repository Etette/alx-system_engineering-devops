#!/usr/bin/python3
"""
Use given REST API (for employer ID)
return information about employer todo list
progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    api_url_usr = api + "users/" + argv[1]
    api_usr_todos = api + "todos?userId=" + argv[1]

    response = requests.get(api_url_usr).json()
    todo = resquests.get(api_url_todos).json()

    complete_tasks = []
    for task in todo:
        if task.get("completed") is not False:
            complete_tasks.append(task.get("title"))

    print("Employer {} is done with tasks ({}/{}):".format(
        response.get("name"), len(complete_tasks), len(todo)))
    for title in complete_tasks:
        print("\t {}".format(title))
