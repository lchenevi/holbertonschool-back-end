#!/usr/bin/python3
"""cré fichier csv avec données d'une api dont l'id est passé en argument"""
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url_api = 'https://jsonplaceholder.typicode.com'
    json_user = requests.get(url_api + "/users/" + id)
    json_todo = requests.get(url_api + "/todos?userId=" + id)

    data_user = json_user.json()
    data_todos = json_todo.json()

    texte = ""
    for todo in data_todos:
        texte = texte + '"' + id + '"'
        texte = texte + ',"' + data_user.get("username") + '"'
        texte = texte + ',"' + str(todo.get("completed")) + '"'
        texte = texte + ',"' + todo.get("title") + '"\n'

    with open(id + ".csv", "w") as file:
        file.write(texte)
