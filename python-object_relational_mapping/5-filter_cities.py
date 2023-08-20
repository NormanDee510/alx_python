#!/usr/bin/env python3
import sys
import MySQLdb


def filter_cities_by_state(username, password, database, state_name):
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

    # Create a parameterized query to retrieve cities of the specified state
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Extract city names and join them
    city_names = [row[0] for row in results]
    cities_string = ", ".join(city_names)

    # Print the results
    print(cities_string)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password>"
              "<database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter and display cities by state
    filter_cities_by_state(username, password, database, state_name)
