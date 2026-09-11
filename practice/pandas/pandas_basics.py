import pandas as pd


# ============================================================
# SECTION 1 - CREATE DATAFRAME
# ============================================================

data = {
    "Name": ["John", "Sarah", "Mike"],
    "Age": [30, 28, 35],
    "Salary": [50000, 80000, 70000]
}

df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME:")
print(df)


# ============================================================
# SECTION 2 - SELECT A COLUMN
# ============================================================

print("\nNAMES:")
print(df["Name"])


# ============================================================
# SECTION 3 - CREATE A CONDITION
# ============================================================

print("\nSALARY >= 60000:")
print(df["Salary"] >= 60000)


# ============================================================
# SECTION 4 - FILTER ROWS
# ============================================================

print("\nEMPLOYEES WITH SALARY >= 60000:")
print(df[df["Salary"] >= 60000])


# ============================================================
# SECTION 5 - AND CONDITION
# Both conditions must be True
# ============================================================

print("\nAGE > 30 AND SALARY > 60000:")
print(df[(df["Age"] > 30) & (df["Salary"] > 60000)])


# ============================================================
# SECTION 6 - OR CONDITION
# At least one condition must be True
# ============================================================

print("\nAGE > 32 OR SALARY > 75000:")
print(df[(df["Age"] > 32) | (df["Salary"] > 75000)])


# ============================================================
# SECTION 7 - LOC
# Select rows using index labels
# ============================================================

print("\nROW WITH INDEX 1:")
print(df.loc[1])

print("\nROWS WITH INDEX 0 AND 2:")
print(df.loc[[0, 2]])


# ============================================================
# SECTION 8 - ILOC
# Select rows using position numbers
# ============================================================

print("\nFIRST TWO ROWS:")
print(df.iloc[0:2])


# ============================================================
# SECTION 9 - SORTING
# ============================================================

print("\nSALARY - LOWEST TO HIGHEST:")
print(df.sort_values("Salary", ascending=True))

print("\nSALARY - HIGHEST TO LOWEST:")
print(df.sort_values("Salary", ascending=False))

print("\nAGE - LOWEST TO HIGHEST:")
print(df.sort_values("Age", ascending=True))

print("\nAGE - HIGHEST TO LOWEST:")
print(df.sort_values("Age", ascending=False))

print("\nSORT BY NAME:")
print(df.sort_values("Name"))

# Store sorted DataFrame
sorted_salary = df.sort_values("Salary", ascending=False)


# ============================================================
# SECTION 10 - ADDING AND REMOVING COLUMNS
# ============================================================

# Add a fixed Bonus column
df["Bonus"] = 5000

# Calculate 10% bonus from salary
df["Calculated_Bonus"] = df["Salary"] * 0.10

# Calculate salary including bonus
df["Salary_With_Bonus"] = df["Salary"] + df["Calculated_Bonus"]

print("\nDATAFRAME WITH BONUS:")
print(df)

# Remove Bonus column
df.drop("Bonus", axis=1, inplace=True)

print("\nAFTER REMOVING BONUS:")
print(df)


# ============================================================
# SECTION 11 - RENAME A COLUMN
# ============================================================

df.rename(columns={"Salary": "Annual_Salary"}, inplace=True)

print("\nAFTER RENAMING SALARY:")
print(df)


# ============================================================
# SECTION 12 - CALCULATE TAX
# ============================================================

# Calculate 10% tax from Annual Salary
df["Tax"] = df["Annual_Salary"] * 0.10

print("\nTAX:")
print(df[["Name", "Annual_Salary", "Tax"]])


# ============================================================
# SECTION 13 - CALCULATE NET SALARY
# ============================================================

# Net Salary = Annual Salary - Tax
df["Net_Salary"] = df["Annual_Salary"] - df["Tax"]

print("\nNET SALARY:")
print(df[["Name", "Annual_Salary", "Tax", "Net_Salary"]])


# ============================================================
# SECTION 14 - FILTER NET SALARY
# ============================================================

print("\nEMPLOYEES WITH NET SALARY ABOVE 60000:")
print(df[df["Net_Salary"] > 60000])


# ============================================================
# SECTION 15 - HIGHEST NET SALARY
# ============================================================

print("\nEMPLOYEE WITH HIGHEST NET SALARY:")
print(df[df["Net_Salary"] == df["Net_Salary"].max()])


# ============================================================
# SECTION 16 - LOWEST NET SALARY
# ============================================================

print("\nEMPLOYEE WITH LOWEST NET SALARY:")
print(df[df["Net_Salary"] == df["Net_Salary"].min()])


# ============================================================
# SECTION 17 - AVERAGE NET SALARY
# ============================================================

print("\nAVERAGE NET SALARY:")
print(df["Net_Salary"].mean())


# ============================================================
# SECTION 18 - NUMBER OF EMPLOYEES
# ============================================================

print("\nNUMBER OF EMPLOYEES:")
print(len(df))


# ============================================================
# SECTION 19 - EMPLOYEES WITH NET SALARY ABOVE 60000
# ============================================================

print("\nNUMBER OF EMPLOYEES WITH NET SALARY ABOVE 60000:")
print(len(df[df["Net_Salary"] > 60000]))


# ============================================================
# SECTION 20 - TOTAL NET SALARY
# ============================================================

print("\nTOTAL NET SALARY:")
print(df["Net_Salary"].sum())


# ============================================================
# SECTION 21 - AVERAGE AGE
# ============================================================

print("\nAVERAGE AGE:")
print(df["Age"].mean())


# ============================================================
# SECTION 22 - TOTAL ANNUAL SALARY
# ============================================================

print("\nTOTAL ANNUAL SALARY:")
print(df["Annual_Salary"].sum())


# ============================================================
# SECTION 23 - AVERAGE ANNUAL SALARY
# ============================================================

print("\nAVERAGE ANNUAL SALARY:")
print(df["Annual_Salary"].mean())



