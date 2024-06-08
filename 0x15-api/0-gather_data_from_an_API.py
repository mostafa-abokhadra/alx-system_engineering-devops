#!/usr/bin/python3
"""requesting and response of api
"""

import requests
import sys

personal_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(sys.argv[1]))
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
