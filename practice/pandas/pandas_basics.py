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