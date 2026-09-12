import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

   

# ============================================================
# SECTION 61 - LOAD REAL GOOGLE PLAY STORE DATA
# ============================================================

# Load the Google Play Store CSV file.
df = pd.read_csv(
    "practice/pandas/data/Google-Playstore.csv/Google-Playstore.csv"
)
df["Rating"] = df["Rating"].replace(0, np.nan)


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

# BUSINESS QUESTION 4:
# Which categories have the most apps?
# This helps us understand competition.

category_analysis = df.groupby("Category").agg({
    "App Name": "count",
    "Rating": "mean",
    "Minimum Installs": "sum"
})

# Sort categories by number of apps
# Highest number of apps = most competition

most_competitive = category_analysis.sort_values(
    "App Name",
    ascending=False
)

print("\nMOST COMPETITIVE CATEGORIES:")
print(most_competitive.head(10))

category_ratings = (
    df.groupby("Category")["Rating"]
      .mean()
      .sort_values(ascending=False)
)

print("\nHIGHEST RATED CATEGORIES:")
print(category_ratings.head(10))


# BUSINESS QUESTION 5:
# Which categories have high demand but relatively low competition?
# This can help us identify potentially attractive market opportunities.

# Total number of apps represents competition.
# Total minimum installs represents market demand.


category_analysis = df.groupby("Category").agg({
    "App Name": "count", # Number of apps = competition
    "Rating": "mean",    # Average rating = user satisfaction
    "Minimum Installs":"sum" # Total installs = market demand
})



# Sort categories by total installs.
# Categories with more installs have higher market demand.
high_demand = category_analysis.sort_values(
    "Minimum Installs",
    ascending=False
)


print("\nHIGHEST DEMAND CATEGORIES:")
print(high_demand.head(10))

# BUSINESS QUESTION 6:
# Which categories have the highest demand per app?
# This helps us compare market demand against competition.

category_analysis["Demand Per App"] = (
    category_analysis["Minimum Installs"] /
    category_analysis["App Name"]
)

# Sort categories from highest demand per app to lowest.

demand_per_app = category_analysis.sort_values(
    "Demand Per App",
    ascending=False
)

print("\nHIGHEST DEMAND PER APP:")
print(demand_per_app.head(10))


# MATPLOTLIB — GRAPH 1
# Show the top 10 categories by total installs.

top_10_demand = high_demand.head(10)

plt.figure(figsize=(12, 8))

plt.bar(
    top_10_demand.index,
    top_10_demand["Minimum Installs"]
)

plt.title("Top 10 Categories by Total Installs")
plt.xlabel("Category")
plt.ylabel("Total Minimum Installs")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()


# MATPLOTLIB — GRAPH 2
# Show the top 10 categories by number of apps.
# This helps us understand which categories have the most competition.


top_10_competition = category_analysis.sort_values(
    "App Name" ,
    ascending=False
).head(10)

plt.figure(figsize=(10,6))

plt.bar(
    top_10_competition.index,
    top_10_demand["App Name"]
)

plt.title("Top 10 Categories by Number of Apps")
plt.xlabel("Category")
plt.ylabel("Number of Apps")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()


# MATPLOTLIB — GRAPH 3
# Compare demand and competition for the top 10
# categories with the highest total installs.

top_10_demand = category_analysis.sort_values(
    "Minimum Installs",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

plt.bar(
    top_10_demand.index,
    top_10_demand["Minimum Installs"]
)

plt.title("Top 10 Categories: Demand")
plt.xlabel("Category")
plt.ylabel("Total Minimum Installs")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()


# MATPLOTLIB — GRAPH 4
# Scatter plot showing the relationship between
# competition and market demand.

plt.figure(figsize=(10, 6))

plt.scatter(
    category_analysis["App Name"],
    category_analysis["Minimum Installs"]
)

plt.title("Competition vs. Market Demand")
plt.xlabel("Number of Apps (Competition)")
plt.ylabel("Total Minimum Installs (Demand)")

plt.tight_layout()

plt.show()

# MATPLOTLIB — GRAPH 5
# Show how apps are distributed across the largest categories.

top_5_categories = category_analysis.sort_values(
    "App Name",
    ascending=False
).head(5)
other_apps = (
    category_analysis["App Name"].sum()
    - top_5_categories["App Name"].sum()
)
pie_data = top_5_categories["App Name"].copy()

pie_data["Other"] = other_apps

plt.figure(figsize=(8, 8))

plt.pie(
    pie_data,
    labels=pie_data.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("App Distribution by Category")

plt.tight_layout()

plt.show()

# MATPLOTLIB — GRAPH 6
# Show the distribution of app ratings.
# This helps us understand how ratings are spread across the apps.

plt.figure(figsize=(10, 6))

plt.hist(
    df["Rating"].dropna(),
    bins=20
)

plt.title("Distribution of App Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Apps")

plt.tight_layout()



