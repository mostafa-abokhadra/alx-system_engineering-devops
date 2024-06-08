#!/usr/bin/python3
"""api to json formating"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    user_id = int(sys.argv[1])
    user_data = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    user_name = user_data.json().get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_list = todo.json()

    dicty = {}
    listy_of_dicty = []
    for item in todo_list:
        if item.get('userId') == user_id:
            dicty["task"] = item.get("title")
            dicty["completed"] = item.get("completed")
            dicty["username"] = user_name
            listy_of_dicty.append(dict(dicty))
            dicty.clear()
    dicty[user_id] = listy_of_dicty

    file_name = str(user_id) + ".json"
    with open(file_name, 'w') as fily:
        fily.write(json.dumps(dicty))
