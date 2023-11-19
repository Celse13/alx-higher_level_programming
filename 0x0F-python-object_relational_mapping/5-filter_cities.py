#!/usr/bin/python3
"""Retrieving the states from the database using ORM."""

import MySQLdb
import sys

if __name__ == "__main__":
    data_base = MySQLdb.connect(
        host="localhost", user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], port=3306
    )
    database_cursor = data_base.cursor()

    query = 'SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s'

    args = (sys.argv[4])

    database_cursor.execute(query, args)

    data_base_rows = database_cursor.fetchall()

    temp = []
    for item in data_base_rows:
        temp.append(item[1])
    print(", ".join(temp))

    database_cursor.close()
    data_base.close()
