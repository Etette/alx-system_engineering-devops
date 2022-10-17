#!/usr/bin/python3
"""
Use given REST API (for employer ID)
return information about employer todo list
progress. export data to CSV format
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    api_url_usr = api + "users/" + argv[1]
    api_url_todos = api + "todos?userId=" + argv[1]

    response = requests.get(api_url_usr).json()
    todo = requests.get(api_url_todos).json()

    filename = argv[1] + ".csv"
    with open(filename, 'w', newline='') as csvfile:
        write_file = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            write_file.writerow([int(argv[1]), response.get("username"),
                                task.get("completed"), task.get("title")])
