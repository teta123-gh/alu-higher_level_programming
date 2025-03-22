#!/usr/bin/python3
"""
Select all records from states table
"""
from sys import argv

import MySQLdb

if __name__ == "__main__":
    username, password, database = argv[1:4]
    search_name = argv[4]
    # default host is 'localhost' and default port is '3306'
    connection = MySQLdb.connect(
        user=username,
        password=password,
        db=database
    )

    cursor = connection.cursor()
    cursor.execute(
        'SELECT * FROM states '
        'WHERE name = %s '
        'ORDER BY states.id', (search_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    connection.close()
