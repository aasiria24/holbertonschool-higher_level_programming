#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table
where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> <mysql password>
                               <database name> <state name searched>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Retrieve all states with the exact name provided by the user, sorted by id
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    # Print all matching rows
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
