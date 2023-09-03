#!/usr/bin/env python3
import sys
import MySQLdb


def filter_states(username, password, database):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE UPPER(name) LIKE 'N%' "
        "ORDER BY id ASC"
    )

    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function to filter and display the states
    filter_states(username, password, database)
