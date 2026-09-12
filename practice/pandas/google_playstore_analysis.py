import pandas as pd


# ============================================================
# SECTION 61 - LOAD REAL GOOGLE PLAY STORE DATA
# ============================================================

# Load the Google Play Store CSV file.
df = pd.read_csv(
    "practice/pandas/data/Google-Playstore.csv/Google-Playstore.csv"
)

# Display the first 5 rows.
print("\nFIRST 5 ROWS:")
print(df.head())

# Display the number of rows and columns.
print("\nDATASET SHAPE:")
print(df.shape)

# Display all column names.
print("\nDATASET COLUMNS:")
print(df.columns)

# Display basic information about the dataset.
print("\nDATASET INFORMATION:")
df.info()

print("\nAPPS BY CATEGORY:")
print(
    df.groupby("Category")["App Name"]
      .count()
      .sort_values(ascending=False)
)

print("\nAPPS BY HIGHEST AVERAGE RATING :")
print(
    df.groupby("Category")["Rating"]
      .mean()
      .sort_values(ascending=False)
)

print("\nCATEGORIES BY TOTAL INSTALLS:")

print(
    df.groupby("Category")["Minimum Installs"]
      .sum()
      .sort_values(ascending=False)
)

print("\nCATEGORY BUSINESS ANALYSIS:")

print(
    df.groupby("Category").agg({
        "App Name": "count",
        "Rating": "mean",
        "Minimum Installs": "sum"
    })
)