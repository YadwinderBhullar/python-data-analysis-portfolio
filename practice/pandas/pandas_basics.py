import pandas as pd


# ============================================================
# 1. CREATE OUR DATA
# ============================================================

# We create a dictionary containing employee information.
data = {
    "Name": ["John", "Sarah", "Mike"],
    "Age": [30, 28, 35],
    "Salary": [50000, 80000, 70000]
}


# ============================================================
# 2. CREATE A PANDAS DATAFRAME
# ============================================================

# pd.DataFrame() converts our dictionary into a table.
df = pd.DataFrame(data)

print("FULL DATAFRAME:")
print(df)


# ============================================================
# 3. SELECT ONE COLUMN
# ============================================================

# df["Name"] selects only the Name column.
print("\nNAMES:")
print(df["Name"])


# ============================================================
# 4. FILTER USING ONE CONDITION
# ============================================================

# This checks which employees have a salary >= $60,000.
#
# The result is True or False for every row.
print("\nSALARY >= $60,000:")
print(df["Salary"] >= 60000)


# ============================================================
# 5. FILTER THE ACTUAL ROWS
# ============================================================

# Putting the condition inside df[...] returns
# only the rows where the condition is True.
print("\nEMPLOYEES WITH SALARY >= $60,000:")
print(df[df["Salary"] >= 60000])


# ============================================================
# 6. FILTER USING AND (&)
# ============================================================

# We want employees who satisfy BOTH conditions:
#
# Age > 30
# AND
# Salary > 60,000
#
# IMPORTANT:
# Each condition must be inside parentheses.
print("\nAGE > 30 AND SALARY > $60,000:")
print(
    df[
        (df["Age"] > 30) &
        (df["Salary"] > 60000)
    ]
)


# ============================================================
# 7. FILTER USING OR (|)
# ============================================================

# We want employees who satisfy AT LEAST ONE condition:
#
# Age > 32
# OR
# Salary > 75,000
#
# | means OR in Pandas.
print("\nAGE > 32 OR SALARY > $75,000:")
print(
    df[
        (df["Age"] > 32) |
        (df["Salary"] > 75000)
    ]
)


# ============================================================
# 8. SELECT SPECIFIC ROWS USING LOC
# ============================================================

# loc uses the INDEX LABEL.
#
# Here we select row 1.
# Row 1 belongs to Sarah.
print("\nROW 1 USING LOC:")
print(df.loc[1])


# ============================================================
# 9. SELECT MULTIPLE ROWS USING LOC
# ============================================================

# We can provide a list of index labels.
#
# [0, 2] means:
# Row 0 -> John
# Row 2 -> Mike
print("\nJOHN AND MIKE:")
print(df.loc[[0, 2]])


# ============================================================
# 10. SELECT ROWS USING ILOC
# ============================================================

# iloc uses INTEGER POSITION.
#
# 0:2 means positions 0 and 1.
# The ending position 2 is NOT included.
print("\nFIRST TWO ROWS USING ILOC:")
print(df.iloc[0:2])

# ============================================================
# SECTION 11: SORTING DATAFRAMES
# ============================================================

# Sort by Salary from lowest to highest
print("\nSALARY - LOWEST TO HIGHEST:")
print(df.sort_values("Salary", ascending=True))


# Sort by Salary from highest to lowest
print("\nSALARY - HIGHEST TO LOWEST:")
print(df.sort_values("Salary", ascending=False))


# Sort by Age from youngest to oldest
print("\nAGE - YOUNGEST TO OLDEST:")
print(df.sort_values("Age", ascending=True))


# Sort by Age from oldest to youngest
print("\nAGE - OLDEST TO YOUNGEST:")
print(df.sort_values("Age", ascending=False))


# Sort names alphabetically
print("\nNAME - ALPHABETICAL ORDER:")
print(df.sort_values("Name"))


# Save the sorted result into a new variable
# This does NOT change the original DataFrame.
sorted_salary = df.sort_values("Salary", ascending=False)

print("\nSAVED SORTED DATA:")
print(sorted_salary)

# ============================================================
# SECTION 12: ADDING AND REMOVING COLUMNS
# ============================================================


# ------------------------------------------------------------
# 1. ADD A NEW COLUMN
# ------------------------------------------------------------

# We can create a new column by assigning a value to it.
#
# Here we add a "Bonus" column.
df["Bonus"] = 5000

print("\nDATAFRAME WITH BONUS COLUMN:")
print(df)


# ------------------------------------------------------------
# 2. CREATE A COLUMN USING AN EXISTING COLUMN
# ------------------------------------------------------------

# We can use an existing column to calculate a new column.
#
# Here we calculate a 10% bonus based on Salary.
df["Calculated_Bonus"] = df["Salary"] * 0.10

print("\nDATAFRAME WITH CALCULATED BONUS:")
print(df)


# ------------------------------------------------------------
# 3. CREATE A NEW COLUMN USING MULTIPLE COLUMNS
# ------------------------------------------------------------

# We can perform calculations using more than one column.
#
# Here we calculate salary after adding the calculated bonus.
df["Salary_With_Bonus"] = df["Salary"] + df["Calculated_Bonus"]

print("\nSALARY WITH BONUS:")
print(df)


# ------------------------------------------------------------
# 4. REMOVE A COLUMN
# ------------------------------------------------------------

# drop() removes a column from the DataFrame.
#
# axis=1 means we are removing a COLUMN.
#
# inplace=True means the original DataFrame is changed.
df.drop("Bonus", axis=1, inplace=True)

print("\nAFTER REMOVING BONUS COLUMN:")
print(df)


# ------------------------------------------------------------
# 5. REMOVE MULTIPLE COLUMNS
# ------------------------------------------------------------

# We can remove more than one column by putting
# the column names inside a list.
#
# Uncomment this if you want to practice:
#
# df.drop(["Calculated_Bonus", "Salary_With_Bonus"], axis=1, inplace=True)
#
# print(df)


# ------------------------------------------------------------
# 6. RENAME A COLUMN
# ------------------------------------------------------------

# rename() allows us to change column names.
#
# Here we change "Salary" to "Annual_Salary".
df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

print("\nAFTER RENAMING SALARY:")
print(df)