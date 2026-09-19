import sqlite3

# ============================================================
# GOOGLE PLAY STORE SQL ANALYSIS
# ============================================================

# Connect to the SQLite database
connection = sqlite3.connect("google_playstore.db")

# Create a cursor
cursor = connection.cursor()

# ------------------------------------------------------------
# BUSINESS QUESTION:
# What are the top 5 app categories by number of applications?
# ------------------------------------------------------------

cursor.execute("""
    SELECT Category, COUNT(*) AS App_Count
    FROM apps
    GROUP BY Category
    ORDER BY App_Count DESC
    LIMIT 5;
""")

# Store results
results = cursor.fetchall()

# Display results
print("\nTop 5 App Categories:")
print("-" * 40)

for row in results:
    print(row)

# Close database connection
connection.close()