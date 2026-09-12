import sqlite3
import pandas as pd

# Path to our Google Play Store
csv_file = r"C:\Users\ysbhu\Desktop\-2026-Python-Practise\practice\pandas\data\Google-Playstore.csv\Google-Playstore.csv"

# Connect to our SQLite database
connection = sqlite3.connect("google_playstore.db")

# Read only the first 10,000 rows
df = pd.read_csv(csv_file, nrows=10000)

# Put the data into a SQL table called "apps"
df.to_sql(
    "apps",
    connection,
    if_exists="replace",
    index=False
)

print("Google Play Store data loaded successfully!")
print("Rows loaded:", len(df))
print("Table created: apps")

# Close the database connection
connection.close()