#!/usr/bin/python3
"""cré fichier json avec données d'une api dont l'id est passé en argument"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url_api = 'https://jsonplaceholder.typicode.com'
    json_user = requests.get(url_api + "/users/" + id)
    json_todo = requests.get(url_api + "/todos?userId=" + id)

    if json_todo.status_code != 200 or json_user.status_code != 200:
        exit(1)

    data_user = json_user.json()
    data_api_todos = json_todo.json()

    liste_todos = []
    for todo in data_api_todos:
        dict_todos = {}

        dict_todos["task"] = todo["title"]
        dict_todos["completed"] = todo["completed"]
        dict_todos["username"] = json_user.json()['username']

        liste_todos.append(dict_todos)

    dict_data_todo = {}
    dict_data_todo[id] = liste_todos

    with open(id + ".json", "w") as file:
        json.dump(dict_data_todo, file)
