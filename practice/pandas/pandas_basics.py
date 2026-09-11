import pandas as pd


# ============================================================
# SECTION 1 - CREATE DATAFRAME
# ============================================================

# Create a dictionary containing our employee data
data = {
    "Name": ["John", "Sarah", "Mike"],
    "Age": [30, 28, 35],
    "Salary": [50000, 80000, 70000]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME:")
print(df)


# ============================================================
# SECTION 2 - SELECT A COLUMN
# ============================================================

# Select only the Name column
print("\nNAMES:")
print(df["Name"])


# ============================================================
# SECTION 3 - CREATE A CONDITION
# ============================================================

# Check which employees have a salary of 60000 or more
# This returns True or False for each row
print("\nSALARY >= 60000:")
print(df["Salary"] >= 60000)


# ============================================================
# SECTION 4 - FILTER ROWS
# ============================================================

# Show only employees whose salary is 60000 or more
print("\nEMPLOYEES WITH SALARY >= 60000:")
print(df[df["Salary"] >= 60000])


# ============================================================
# SECTION 5 - AND CONDITION
# ============================================================

# Both conditions must be True
# Age must be greater than 30 AND salary greater than 60000
print("\nAGE > 30 AND SALARY > 60000:")
print(df[(df["Age"] > 30) & (df["Salary"] > 60000)])


# ============================================================
# SECTION 6 - OR CONDITION
# ============================================================

# At least one condition must be True
# Age greater than 32 OR salary greater than 75000
print("\nAGE > 32 OR SALARY > 75000:")
print(df[(df["Age"] > 32) | (df["Salary"] > 75000)])


# ============================================================
# SECTION 7 - LOC
# ============================================================

# loc selects rows using index labels
print("\nROW WITH INDEX 1:")
print(df.loc[1])

# Select multiple rows using their index labels
print("\nROWS WITH INDEX 0 AND 2:")
print(df.loc[[0, 2]])


# ============================================================
# SECTION 8 - ILOC
# ============================================================

# iloc selects rows using their position
# 0:2 means positions 0 and 1
print("\nFIRST TWO ROWS:")
print(df.iloc[0:2])


# ============================================================
# SECTION 9 - SORTING
# ============================================================

# Sort salary from lowest to highest
print("\nSALARY - LOWEST TO HIGHEST:")
print(df.sort_values("Salary", ascending=True))

# Sort salary from highest to lowest
print("\nSALARY - HIGHEST TO LOWEST:")
print(df.sort_values("Salary", ascending=False))

# Sort age from lowest to highest
print("\nAGE - LOWEST TO HIGHEST:")
print(df.sort_values("Age", ascending=True))

# Sort age from highest to lowest
print("\nAGE - HIGHEST TO LOWEST:")
print(df.sort_values("Age", ascending=False))

# Sort names alphabetically
print("\nSORT BY NAME:")
print(df.sort_values("Name"))

# Store a sorted DataFrame in a variable
sorted_salary = df.sort_values("Salary", ascending=False)


# ============================================================
# SECTION 10 - ADDING AND REMOVING COLUMNS
# ============================================================

# Add a fixed bonus of $5,000 to every employee
df["Bonus"] = 5000

# Calculate a 10% bonus based on salary
df["Calculated_Bonus"] = df["Salary"] * 0.10

# Calculate salary plus calculated bonus
df["Salary_With_Bonus"] = df["Salary"] + df["Calculated_Bonus"]

print("\nDATAFRAME WITH BONUS:")
print(df)

# Remove the original Bonus column
# axis=1 means we are removing a column
df.drop("Bonus", axis=1, inplace=True)

print("\nAFTER REMOVING BONUS:")
print(df)


# ============================================================
# SECTION 11 - RENAME A COLUMN
# ============================================================

# Rename Salary to Annual_Salary
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

# Show employees whose net salary is greater than $60,000
print("\nEMPLOYEES WITH NET SALARY ABOVE 60000:")
print(df[df["Net_Salary"] > 60000])


# ============================================================
# SECTION 15 - HIGHEST NET SALARY
# ============================================================

# Find the highest net salary
highest_net_salary = df["Net_Salary"].max()

# Filter the DataFrame to show the employee
# whose salary equals the highest salary
print("\nEMPLOYEE WITH HIGHEST NET SALARY:")
print(df[df["Net_Salary"] == highest_net_salary])


# ============================================================
# SECTION 16 - LOWEST NET SALARY
# ============================================================

# Find the lowest net salary
lowest_net_salary = df["Net_Salary"].min()

# Show the employee with the lowest net salary
print("\nEMPLOYEE WITH LOWEST NET SALARY:")
print(df[df["Net_Salary"] == lowest_net_salary])


# ============================================================
# SECTION 17 - AVERAGE NET SALARY
# ============================================================

# Calculate the average net salary
print("\nAVERAGE NET SALARY:")
print(df["Net_Salary"].mean())


# ============================================================
# SECTION 18 - NUMBER OF EMPLOYEES
# ============================================================

# len(df) counts the total number of rows
print("\nNUMBER OF EMPLOYEES:")
print(len(df))


# ============================================================
# SECTION 19 - NUMBER OF EMPLOYEES WITH NET SALARY ABOVE 60000
# ============================================================

# First filter employees with net salary above 60000
# Then len() counts how many rows remain
print("\nNUMBER OF EMPLOYEES WITH NET SALARY ABOVE 60000:")
print(len(df[df["Net_Salary"] > 60000]))


# ============================================================
# SECTION 20 - TOTAL NET SALARY
# ============================================================

# sum() adds all Net Salary values
print("\nTOTAL NET SALARY:")
print(df["Net_Salary"].sum())


# ============================================================
# SECTION 21 - AVERAGE AGE
# ============================================================

# mean() calculates the average age
print("\nAVERAGE AGE:")
print(df["Age"].mean())


# ============================================================
# SECTION 22 - TOTAL ANNUAL SALARY
# ============================================================

# sum() adds all Annual Salary values
print("\nTOTAL ANNUAL SALARY:")
print(df["Annual_Salary"].sum())


# ============================================================
# SECTION 23 - AVERAGE ANNUAL SALARY
# ============================================================

# mean() calculates the average Annual Salary
print("\nAVERAGE ANNUAL SALARY:")
print(df["Annual_Salary"].mean())


# ============================================================
# SECTION 24 - ADD DEPARTMENT
# ============================================================

# Add a Department column
df["Department"] = ["IT", "HR", "IT"]

print("\nDATAFRAME WITH DEPARTMENT:")
print(df)


# ============================================================
# SECTION 25 - GROUPBY
# ============================================================

# groupby() groups rows based on a column
#
# Here we are grouping employees by Department:
#
# HR → Sarah
# IT → John, Mike
#
# At this point Pandas creates groups,
# but we haven't asked for a calculation yet.

print("\nGROUP BY DEPARTMENT:")
print(df.groupby("Department"))


# ============================================================
# SECTION 26 - AVERAGE SALARY BY DEPARTMENT
# ============================================================

# groupby Department
# select Annual_Salary
# calculate the average using mean()

print("\nAVERAGE SALARY BY DEPARTMENT:")
print(df.groupby("Department")["Annual_Salary"].mean())


# ============================================================
# SECTION 27 - TOTAL SALARY BY DEPARTMENT
# ============================================================

# Calculate the total Annual Salary
# for each department

print("\nTOTAL SALARY BY DEPARTMENT:")
print(df.groupby("Department")["Annual_Salary"].sum())


# ============================================================
# SECTION 28 - NUMBER OF EMPLOYEES BY DEPARTMENT
# ============================================================

# size() counts the number of rows
# inside each department group

print("\nNUMBER OF EMPLOYEES BY DEPARTMENT:")
print(df.groupby("Department").size())


# ============================================================
# SECTION 29 - HIGHEST SALARY BY DEPARTMENT
# ============================================================

# Find the highest Annual Salary
# in each department

print("\nHIGHEST SALARY BY DEPARTMENT:")
print(df.groupby("Department")["Annual_Salary"].max())


# ============================================================
# SECTION 30 - LOWEST SALARY BY DEPARTMENT
# ============================================================

# Find the lowest Annual Salary
# in each department

print("\nLOWEST SALARY BY DEPARTMENT:")

# Store the result in a variable
lowest_salary_by_department = (
    df.groupby("Department")["Annual_Salary"].min()
)

print(lowest_salary_by_department)


# ============================================================
# END OF CURRENT PANDAS PRACTICE
# ============================================================