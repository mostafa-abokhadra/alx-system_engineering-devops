#!/usr/bin/python3
"""last big json task"""


if __name__ == '__main__':
    import json
    import requests

    req = requests.get('https://jsonplaceholder.typicode.com/users')
    personal_data = req.json()

    req2 = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = req2.json()

    user_dict = {}
    user_list = []
    final_dictionary = {}

    for item in personal_data:
        username = item.get('username')
        user_id = item.get('id')
        for dicty in todo_list:
            if dicty.get('userId') == user_id:
                user_dict['username'] = username
                user_dict["task"] = dicty.get('title')
                user_dict["completed"] = dicty.get("completed")
                user_list.append(dict(user_dict))
        final_dictionary[user_id] = list(user_list)
        user_list.clear()
        user_dict.clear()

        with open("todo_all_employees.json", 'w') as fily:
            fily.write(json.dumps(final_dictionary))
