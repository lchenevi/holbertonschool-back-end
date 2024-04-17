#!/usr/bin/python3
"""cré fichier json avec données d'une api de tous les id user dans /users"""
import json
import requests


if __name__ == "__main__":

    url_api = 'https://jsonplaceholder.typicode.com'
    json_user = requests.get(url_api + "/users")
    json_todo = requests.get(url_api + "/todos")

    if json_todo.status_code != 200 or json_user.status_code != 200:
        exit(1)

    data_user = json_user.json()
    data_api_todos = json_todo.json()

    dict_data_todo = {}

    for user in data_user:
        id = user['id']

        liste_todos = []
        for todo in data_api_todos:
            if todo['userId'] == id:
                dict_todos = {}
                dict_todos["task"] = todo["title"]
                dict_todos["completed"] = todo["completed"]
                dict_todos["username"] = user['username']

                liste_todos.append(dict_todos)

        dict_data_todo[id] = liste_todos

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict_data_todo, file)
