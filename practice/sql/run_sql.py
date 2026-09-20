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
    SELECT
        Rating_Category,
        COUNT(*) AS App_Count,
        ROUND(COUNT(*) * 100.0 / 10000, 2) AS Percentage
    FROM (
        SELECT
            CASE
                WHEN Rating >= 4.5 THEN 'Excellent'
                WHEN Rating >= 4.0 THEN 'Good'
                WHEN Rating >= 3.0 THEN 'Average'
                ELSE 'Poor'
            END AS Rating_Category
        FROM apps
    )
    GROUP BY Rating_Category
    ORDER BY App_Count DESC;
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