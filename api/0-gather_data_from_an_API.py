#!/usr/bin/python3
"""get data from an api"""
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url_api = 'https://jsonplaceholder.typicode.com'
    json_user = requests.get(url_api + "/users/" + id)
    json_todo = requests.get(url_api + "/todos?userId=" + id)

    data_user = json_user.json()
    data_todos = json_todo.json()

    fait = 0
    for todo in data_todos:
        if todo.get('completed'):
            fait += 1

    str = "Employee {} ".format(data_user.get('name'))
    str = str + "is done with tasks({}/{}):".format(fait, len(data_todos))

    print(str)
    for todo in data_todos:
        if todo.get('completed'):
            print("\t " + todo.get('title'))
