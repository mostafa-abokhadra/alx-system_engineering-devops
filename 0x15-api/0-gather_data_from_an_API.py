#!/usr/bin/python3
"""requesting and response of api
"""

if __name__ == '__main__':
    import requests
    import sys

    user_id = int(sys.argv[1])
    personal_data = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
    employee = personal_data.json()

    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos')
    todo_list = todo_data.json()

    completed = 0
    total = 0
    completed_list = []

    for item in todo_list:
        if item.get('userId') == int(sys.argv[1]):
            total += 1
            if item.get('completed'):
                completed += 1
                completed_list.append(item.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), completed, total))
    for done in completed_list:
        print("\t " + done)
