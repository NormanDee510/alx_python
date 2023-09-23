import MySQLdb
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 4:
    sys.exit("Usage: {} username password database".format(sys.argv[0]))

# Extract command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

try:
    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to select states starting with a capital letter 'N'
    query = "SELECT * FROM states WHERE name REGEXP '^[N]' ORDER BY id"
    cursor.execute(query)

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except MySQLdb.Error as e:
    sys.exit("MySQL Error: {}".format(e))

finally:
    # Close the database connection
    if db:
        db.close()
