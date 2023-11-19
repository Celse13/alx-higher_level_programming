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
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id;"
    database_cursor.execute(query)

    data_base_rows = database_cursor.fetchall()

    for item in data_base_rows:
        print(item)

    database_cursor.close()
    data_base.close()
