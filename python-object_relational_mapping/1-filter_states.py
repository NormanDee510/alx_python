#!/usr/bin/env python3
import sys
import MySQLdb

def filter_states(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor
    cursor = db.cursor()

    # Execute the query to retrieve states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE LOWER(name) LIKE 'n%' ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Call the function to filter and display the states
    filter_states(username, password, database)
