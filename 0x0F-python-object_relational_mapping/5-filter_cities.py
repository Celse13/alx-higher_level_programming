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

    query = (
        "SELECT name FROM cities "
        "WHERE state_id = (SELECT id FROM states WHERE name LIKE BINARY %s) "
        "ORDER BY cities.id ASC")
    args = (sys.argv[4] + '%',)

    database_cursor.execute(query, args)

    data_base_rows = database_cursor.fetchall()

    temp = ()

    for item in data_base_rows:
        temp += item
    print(*temp, sep=", ")

    database_cursor.close()
    data_base.close()
