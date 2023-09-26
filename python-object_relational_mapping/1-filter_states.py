#!/usr/bin/python3
# This script is meant to filter states names that begin with letter N
# Imports module MySQLdb
import MySQLdb
import sys

def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]

    # Connect to the MySQL database
    database = MySQLdb.connect(
        host='localhost',  # Corrected 'localHost' to 'localhost'
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    # Create a cursor object
    curs = database.cursor()

    # Execute the SQL query to select states starting with a capital letter 'N'
    curs.execute("SELECT * FROM states "
                 "WHERE name LIKE 'N%' AND "  # Corrected AND syntax
                 "BINARY name NOT LIKE 'n%' "  # Added space before AND
                 "ORDER BY states.id ASC")

    # Fetch and print the results
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()

    # Close the database connection
    database.close()

if __name__ == "__main__":
    main()
