import sqlite3

# Connect to our SQLite database
connection = sqlite3.connect("google_playstore.db")

# Create a cursor to execute SQL
cursor = connection.cursor()

# Run our first SQL query
cursor.execute("""
    SELECT "App Name", Category, Rating
FROM apps;
""")

# Store the query results
results = cursor.fetchall()

# Display the first 5 rows
for row in results[:5]:
    print(row)

# Close the database connection
connection.close()