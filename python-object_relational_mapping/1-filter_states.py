#!/usr/bin/python3
"""
Lists all states with a name starting with N (uppercase)
Takes 3 arguments: mysql username, password and database name
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor
    cursor = db.cursor()

    # Execute query
    cursor.execute(
        "SELECT * FROM states "
        "WHERE name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    # Fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connections
    cursor.close()
    db.close()
