#!/usr/bin/python3
# This script is meant to filter states where names matches argument
# Imports module MySQLdb
import MySQLdb
import sys


def main():
    database_name = sys.argv[3]
    username = sys.argv[1]
    password = sys.argv[2]
    name_search = sys.argv[4]

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
                 "WHERE name = '{}' AND " 
                 "name LIKE 'N%' AND " 
                 "BINARY name NOT LIKE 'n%' "  
                 "ORDER BY id ASC".format(name_search))
    
    # Fetch and print the results
    rows = curs.fetchall()
    for row in rows:
        print(row)

    curs.close()


    if __name__ == "__main__":
        main()
    