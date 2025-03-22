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
        'SELECT cities.id, cities.name , states.name '
        'FROM states INNER JOIN cities '
        'ON states.id = cities.state_id WHERE states.name = %s '
        'ORDER BY cities.id', (search_name,))
    states = cursor.fetchall()

    for i in range(len(states)):
        print(states[i][1], end=", " if i + 1 < len(states) else "")
    print("")
    connection.close()
