#!/usr/bin/env python3
import sys
import MySQLdb

"""
This script connects to a MySQL database and retrieves states' information from the 'states' table.
It takes three arguments: mysql username, mysql password, and database name.
"""

def get_states(username, password, database):
    """
    Retrieves and displays information about states from the database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database.

    Returns:
        None
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor
    cursor = db.cursor()

    # Execute the query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    """ Main entry point of the script."""
    
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Call the function to get and display the states
    get_states(username, password, database)