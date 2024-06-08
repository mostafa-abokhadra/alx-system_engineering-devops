#!/usr/bin/python3
"""converting to csv files"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    user_id = int(sys.argv[1])
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    user_name = user.json().get('username')

    todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos/'.format(user_id))
    todo_list = todos.json()
    task_dict = {}
    for item in todo_list:
        if int(item.get('userId')) == user_id:
            task_dict[item.get('title')] = item.get('completed')

    listy = []
    list_of_listy = []

    for key, value in task_dict.items():
        listy.append(user_id)
        listy.append(user_name)
        listy.append(value)
        listy.append(key)
        list_of_listy.append(list(listy))
        listy.clear()

    file_name = str(user_id) + ".csv"
    output_file = open(file_name, 'w')
    outputWriter = csv.writer(
            output_file, quotechar='"', quoting=csv.QUOTE_ALL)

    for listy in list_of_listy:
        outputWriter.writerow(listy)
    output_file.close()
