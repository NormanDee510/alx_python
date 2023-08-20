#!/usr/bin/env python3
import sys
import MySQLdb


def safe_filter_states(username, password, database, state_name):
    # Connect to the MySQL server
    db = MySQLdb.connect(
    host="localhost", 
    port=3306, 
    user=username, 
    passwd=password, 
    db=database
    )

    # Create a cursor
    cursor = db.cursor()

    # Create a parameterized query to retrieve states matching the state name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    
    # Execute the query with a tuple containing the state name as the parameter
    cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    
    # Call the function to filter and display the states
    safe_filter_states(username, password, database, state_name)