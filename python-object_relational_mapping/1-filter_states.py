import MySQLdb
import sys

def list_states(username, password, database_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database_name)
        
        """Create a cursor object to interact with the database"""
        cursor = db.cursor()

        # Execute the SQL query to retrieve states
        query = "SELECT * FROM states where BINARY name like 'N%' ORDER BY states.id ASC"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close the cursor and the database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(username, password, database_name)