import pandas as pd


# ============================================================
# SECTION 1 - CREATE DATAFRAME
# ============================================================

# Create a dictionary containing employee data.
data = {
    "Name": ["John", "Sarah", "Mike"],
    "Age": [30, 28, 35],
    "Salary": [50000, 80000, 70000]
}

# Convert the dictionary into a Pandas DataFrame.
df = pd.DataFrame(data)

print("\nORIGINAL DATAFRAME:")
print(df)


# ============================================================
# SECTION 2 - SELECT A COLUMN
# ============================================================

# Select only the Name column.
print("\nNAMES:")
print(df["Name"])


# ============================================================
# SECTION 3 - CREATE A CONDITION
# ============================================================

# Check which employees have a salary of $60,000 or more.
# This returns True or False for every row.

print("\nSALARY >= 60000:")
print(df["Salary"] >= 60000)


# ============================================================
# SECTION 4 - FILTER ROWS
# ============================================================

# Show only employees whose salary is $60,000 or more.

print("\nEMPLOYEES WITH SALARY >= 60000:")
print(df[df["Salary"] >= 60000])


# ============================================================
# SECTION 5 - AND CONDITION
# ============================================================

# Both conditions must be True.
#
# Age must be greater than 30
# AND
# Salary must be greater than 60000.

print("\nAGE > 30 AND SALARY > 60000:")
print(
    df[
        (df["Age"] > 30) &
        (df["Salary"] > 60000)
    ]
)


# ============================================================
# SECTION 6 - OR CONDITION
# ============================================================

# At least one condition must be True.
#
# Age greater than 32
# OR
# Salary greater than 75000.

print("\nAGE > 32 OR SALARY > 75000:")
print(
    df[
        (df["Age"] > 32) |
        (df["Salary"] > 75000)
    ]
)


# ============================================================
# SECTION 7 - LOC
# ============================================================

# loc selects rows using index labels.

print("\nROW WITH INDEX 1:")
print(df.loc[1])

# Select multiple rows using their index labels.

print("\nROWS WITH INDEX 0 AND 2:")
print(df.loc[[0, 2]])


# ============================================================
# SECTION 8 - ILOC
# ============================================================

# iloc selects rows using their integer position.
#
# 0:2 means positions 0 and 1.
# Position 2 is not included.

print("\nFIRST TWO ROWS:")
print(df.iloc[0:2])


# ============================================================
# SECTION 9 - SORTING
# ============================================================

# Sort salary from lowest to highest.

print("\nSALARY - LOWEST TO HIGHEST:")
print(
    df.sort_values(
        "Salary",
        ascending=True
    )
)

# Sort salary from highest to lowest.

print("\nSALARY - HIGHEST TO LOWEST:")
print(
    df.sort_values(
        "Salary",
        ascending=False
    )
)

# Sort age from lowest to highest.

print("\nAGE - LOWEST TO HIGHEST:")
print(
    df.sort_values(
        "Age",
        ascending=True
    )
)

# Sort age from highest to lowest.

print("\nAGE - HIGHEST TO LOWEST:")
print(
    df.sort_values(
        "Age",
        ascending=False
    )
)

# Sort names alphabetically.

print("\nSORT BY NAME:")
print(df.sort_values("Name"))

# Store a sorted DataFrame in a variable.

sorted_salary = df.sort_values(
    "Salary",
    ascending=False
)


# ============================================================
# SECTION 10 - ADDING COLUMNS
# ============================================================

# Add a fixed bonus of $5,000 to every employee.

df["Bonus"] = 5000

# Calculate a 10% bonus based on salary.

df["Calculated_Bonus"] = df["Salary"] * 0.10

# Calculate salary plus calculated bonus.

df["Salary_With_Bonus"] = (
    df["Salary"] +
    df["Calculated_Bonus"]
)

print("\nDATAFRAME WITH BONUS:")
print(df)


# ============================================================
# SECTION 11 - REMOVE A COLUMN
# ============================================================

# Remove the original fixed Bonus column.
#
# axis=1 means we are removing a column.
# inplace=True changes the original DataFrame.

df.drop(
    "Bonus",
    axis=1,
    inplace=True
)

print("\nAFTER REMOVING BONUS:")
print(df)


# ============================================================
# SECTION 12 - RENAME A COLUMN
# ============================================================

# Rename Salary to Annual_Salary.

df.rename(
    columns={
        "Salary": "Annual_Salary"
    },
    inplace=True
)

print("\nAFTER RENAMING SALARY:")
print(df)


# ============================================================
# SECTION 13 - CALCULATE TAX
# ============================================================

# Calculate 10% tax from Annual Salary.

df["Tax"] = (
    df["Annual_Salary"] * 0.10
)

print("\nTAX:")
print(
    df[
        [
            "Name",
            "Annual_Salary",
            "Tax"
        ]
    ]
)


# ============================================================
# SECTION 14 - CALCULATE NET SALARY
# ============================================================

# Net Salary = Annual Salary - Tax.

df["Net_Salary"] = (
    df["Annual_Salary"] -
    df["Tax"]
)

print("\nNET SALARY:")
print(
    df[
        [
            "Name",
            "Annual_Salary",
            "Tax",
            "Net_Salary"
        ]
    ]
)


# ============================================================
# SECTION 15 - FILTER NET SALARY
# ============================================================

# Show employees whose net salary is greater than $60,000.

print("\nEMPLOYEES WITH NET SALARY ABOVE 60000:")
print(
    df[
        df["Net_Salary"] > 60000
    ]
)


# ============================================================
# SECTION 16 - HIGHEST NET SALARY
# ============================================================

# Find the highest net salary.

highest_net_salary = df["Net_Salary"].max()

print("\nEMPLOYEE WITH HIGHEST NET SALARY:")

print(
    df[
        df["Net_Salary"] == highest_net_salary
    ]
)


# ============================================================
# SECTION 17 - LOWEST NET SALARY
# ============================================================

# Find the lowest net salary.

lowest_net_salary = df["Net_Salary"].min()

print("\nEMPLOYEE WITH LOWEST NET SALARY:")

print(
    df[
        df["Net_Salary"] == lowest_net_salary
    ]
)


# ============================================================
# SECTION 18 - AVERAGE NET SALARY
# ============================================================

# mean() calculates the average.

print("\nAVERAGE NET SALARY:")
print(
    df["Net_Salary"].mean()
)


# ============================================================
# SECTION 19 - NUMBER OF EMPLOYEES
# ============================================================

# len(df) counts the number of rows.

print("\nNUMBER OF EMPLOYEES:")
print(len(df))


# ============================================================
# SECTION 20 - NUMBER ABOVE 60000
# ============================================================

# First filter the employees.
# Then len() counts the remaining rows.

print(
    "\nNUMBER OF EMPLOYEES WITH NET SALARY ABOVE 60000:"
)

print(
    len(
        df[
            df["Net_Salary"] > 60000
        ]
    )
)


# ============================================================
# SECTION 21 - TOTAL NET SALARY
# ============================================================

# sum() adds all Net Salary values.

print("\nTOTAL NET SALARY:")
print(
    df["Net_Salary"].sum()
)


# ============================================================
# SECTION 22 - AVERAGE AGE
# ============================================================

print("\nAVERAGE AGE:")
print(
    df["Age"].mean()
)


# ============================================================
# SECTION 23 - TOTAL ANNUAL SALARY
# ============================================================

print("\nTOTAL ANNUAL SALARY:")
print(
    df["Annual_Salary"].sum()
)


# ============================================================
# SECTION 24 - AVERAGE ANNUAL SALARY
# ============================================================

print("\nAVERAGE ANNUAL SALARY:")
print(
    df["Annual_Salary"].mean()
)


# ============================================================
# SECTION 25 - ADD DEPARTMENT
# ============================================================

# Add a Department column.

df["Department"] = [
    "IT",
    "HR",
    "IT"
]

print("\nDATAFRAME WITH DEPARTMENT:")
print(df)


# ============================================================
# SECTION 26 - BASIC GROUPBY
# ============================================================

# groupby() groups rows based on a column.
#
# Here employees are grouped by Department.

print("\nGROUP BY DEPARTMENT:")
print(
    df.groupby("Department")
)


# ============================================================
# SECTION 27 - AVERAGE SALARY BY DEPARTMENT
# ============================================================

print("\nAVERAGE SALARY BY DEPARTMENT:")

print(
    df.groupby("Department")[
        "Annual_Salary"
    ].mean()
)


# ============================================================
# SECTION 28 - TOTAL SALARY BY DEPARTMENT
# ============================================================

print("\nTOTAL SALARY BY DEPARTMENT:")

print(
    df.groupby("Department")[
        "Annual_Salary"
    ].sum()
)


# ============================================================
# SECTION 29 - NUMBER OF EMPLOYEES BY DEPARTMENT
# ============================================================

# size() counts rows in each group.

print("\nNUMBER OF EMPLOYEES BY DEPARTMENT:")

print(
    df.groupby("Department").size()
)


# ============================================================
# SECTION 30 - HIGHEST SALARY BY DEPARTMENT
# ============================================================

print("\nHIGHEST SALARY BY DEPARTMENT:")

print(
    df.groupby("Department")[
        "Annual_Salary"
    ].max()
)


# ============================================================
# SECTION 31 - LOWEST SALARY BY DEPARTMENT
# ============================================================

print("\nLOWEST SALARY BY DEPARTMENT:")

print(
    df.groupby("Department")[
        "Annual_Salary"
    ].min()
)


# ============================================================
# SECTION 32 - MULTIPLE GROUPBY CALCULATIONS
# ============================================================

# agg() allows us to perform several calculations
# at the same time.

print("\nMULTIPLE SALARY CALCULATIONS BY DEPARTMENT:")

result = (
    df.groupby("Department")[
        "Annual_Salary"
    ].agg(
        [
            "mean",
            "sum",
            "max",
            "min"
        ]
    )
)

print(result)


# ============================================================
# SECTION 33 - MULTIPLE COLUMNS WITH GROUPBY
# ============================================================

# Calculate the average of both Annual Salary
# and Net Salary for each department.

print("\nAVERAGE SALARY AND NET SALARY BY DEPARTMENT:")

result = (
    df.groupby("Department")[
        [
            "Annual_Salary",
            "Net_Salary"
        ]
    ].mean()
)

print(result)


# ============================================================
# SECTION 34 - DIFFERENT CALCULATIONS
# ============================================================

# We can use different calculations
# for different columns.

print("\nAVERAGE ANNUAL SALARY AND HIGHEST NET SALARY:")

result = (
    df.groupby("Department").agg(
        {
            "Annual_Salary": "mean",
            "Net_Salary": "max"
        }
    )
)

print(result)


# ============================================================
# SECTION 35 - DEPARTMENT SUMMARY
# ============================================================

print("\nDEPARTMENT SUMMARY:")

result = (
    df.groupby("Department").agg(
        {
            "Annual_Salary": "sum",
            "Net_Salary": "min",
            "Age": "mean"
        }
    )
)

print(result)


# ============================================================
# SECTION 36 - MISSING DATA
# ============================================================

# Create a missing salary.

df.loc[1, "Annual_Salary"] = None

print("\nDATAFRAME WITH MISSING SALARY:")
print(df)


# ============================================================
# SECTION 37 - FIND MISSING VALUES
# ============================================================

# isna() identifies missing values.

print("\nMISSING VALUES:")
print(df.isna())


# ============================================================
# SECTION 38 - COUNT MISSING VALUES
# ============================================================

# sum() counts the True values.

print("\nNUMBER OF MISSING VALUES:")
print(df.isna().sum())


# ============================================================
# SECTION 39 - SHOW ROWS WITH MISSING SALARY
# ============================================================

print("\nEMPLOYEES WITH MISSING SALARY:")

missing_salary = df[
    df["Annual_Salary"].isna()
]

print(missing_salary)


# ============================================================
# SECTION 40 - FILL MISSING VALUE
# ============================================================

# Fill missing salary with $80,000.

df["Annual_Salary"] = (
    df["Annual_Salary"].fillna(80000)
)

print("\nAFTER FILLING MISSING SALARY:")
print(df)


# ============================================================
# SECTION 41 - REMOVE ROWS WITH MISSING VALUES
# ============================================================

# dropna() removes rows containing missing values.

clean_df = df.dropna()

print("\nDATAFRAME AFTER DROPPING MISSING VALUES:")
print(clean_df)


# ============================================================
# SECTION 42 - FILL MISSING VALUE WITH AVERAGE
# ============================================================

# Find the average salary.

average_salary = (
    df["Annual_Salary"].mean()
)

print("\nAVERAGE SALARY:")
print(average_salary)

# Fill missing values with the average salary.

df["Annual_Salary"] = (
    df["Annual_Salary"].fillna(
        average_salary
    )
)


# ============================================================
# SECTION 43 - DUPLICATES
# ============================================================

# duplicated() checks for duplicate rows.

print("\nDUPLICATE ROWS:")
print(df.duplicated())


# Count duplicate rows.

print("\nNUMBER OF DUPLICATE ROWS:")
print(
    df.duplicated().sum()
)


# Remove duplicate rows.

df = df.drop_duplicates()


# ============================================================
# SECTION 44 - CLEAN TEXT DATA
# ============================================================

# Create a separate DataFrame containing messy names.

df_names = pd.DataFrame(
    {
        "Name": [
            " John",
            "Sarah ",
            " mike",
            "DAVID "
        ]
    }
)

print("\nMESSY NAMES:")
print(df_names)


# Remove spaces before and after the name.

df_names["Name"] = (
    df_names["Name"].str.strip()
)


# Convert names to title case.

df_names["Name"] = (
    df_names["Name"].str.title()
)

print("\nCLEANED NAMES:")
print(df_names)


# ============================================================
# SECTION 45 - LOWERCASE AND UPPERCASE
# ============================================================

# Convert names to lowercase.

df_names["Name_Lower"] = (
    df_names["Name"].str.lower()
)

# Convert names to uppercase.

df_names["Name_Upper"] = (
    df_names["Name"].str.upper()
)

print("\nLOWERCASE AND UPPERCASE:")
print(df_names)


# ============================================================
# SECTION 46 - CLEAN REALISTIC EMPLOYEE DATA
# ============================================================

employee_data = {
    "Name": [
        " john ",
        "SARAH",
        " mike ",
        "David "
    ],

    "Department": [
        " it ",
        "HR",
        " IT",
        "hr "
    ],

    "Salary": [
        50000,
        60000,
        70000,
        55000
    ]
}

employees = pd.DataFrame(employee_data)

print("\nMESSY EMPLOYEE DATA:")
print(employees)


# Clean employee names.

employees["Name"] = (
    employees["Name"]
    .str.strip()
    .str.title()
)


# Clean department names.

employees["Department"] = (
    employees["Department"]
    .str.strip()
    .str.upper()
)

print("\nCLEANED EMPLOYEE DATA:")
print(employees)


# ============================================================
# SECTION 47 - GROUP CLEANED DATA
# ============================================================

print("\nAVERAGE SALARY BY DEPARTMENT:")

print(
    employees.groupby("Department")[
        "Salary"
    ].mean()
)


print("\nTOTAL SALARY BY DEPARTMENT:")

print(
    employees.groupby("Department")[
        "Salary"
    ].sum()
)


print("\nEMPLOYEE COUNT BY DEPARTMENT:")

print(
    employees.groupby("Department").size()
)


print("\nHIGHEST SALARY BY DEPARTMENT:")

print(
    employees.groupby("Department")[
        "Salary"
    ].max()
)


print("\nLOWEST SALARY BY DEPARTMENT:")

print(
    employees.groupby("Department")[
        "Salary"
    ].min()
)


# ============================================================
# SECTION 48 - DEPARTMENT SALARY SUMMARY
# ============================================================

print("\nDEPARTMENT SALARY SUMMARY:")

result = (
    employees.groupby("Department")[
        "Salary"
    ].agg(
        [
            "mean",
            "sum",
            "max",
            "min"
        ]
    )
)

print(result)


# ============================================================
# SECTION 49 - CALCULATE BONUS
# ============================================================

# Calculate a 10% bonus for every employee.

employees["Bonus"] = (
    employees["Salary"] * 0.10
)

print("\nEMPLOYEES WITH BONUS:")
print(employees)


# ============================================================
# SECTION 50 - TOTAL COMPENSATION
# ============================================================

# Total Compensation =
# Salary + Bonus

employees["Total_Compensation"] = (
    employees["Salary"] +
    employees["Bonus"]
)

print("\nTOTAL COMPENSATION:")
print(employees)


# ============================================================
# SECTION 51 - READ CSV FILE
# ============================================================

# read_csv() loads data from a CSV file
# into a Pandas DataFrame.
#
# Example:
#
# df_csv = pd.read_csv("employees.csv")
#
# print(df_csv)


# ============================================================
# SECTION 52 - SAVE TO CSV
# ============================================================

# to_csv() saves a DataFrame as a CSV file.
#
# index=False means:
# Do not save Pandas' row numbers.

# employees.to_csv(
#     "employees_cleaned.csv",
#     index=False
# )


# ============================================================
# SECTION 53 - READ EXCEL FILE
# ============================================================

# read_excel() loads an Excel file.
#
# Example:
#
# df_excel = pd.read_excel("employees.xlsx")
#
# print(df_excel)


# ============================================================
# SECTION 54 - SAVE TO EXCEL
# ============================================================

# to_excel() saves a DataFrame as an Excel file.
#
# index=False prevents Pandas' row numbers
# from becoming an extra Excel column.

# employees.to_excel(
#     "employees_cleaned.xlsx",
#     index=False
# )


# ============================================================
# SECTION 55 - ADVANCED FILTERING WITH isin()
# ============================================================

# isin() checks whether a value exists
# inside a list of values.

print("\nEMPLOYEES IN IT OR HR:")

print(
    employees[
        employees["Department"].isin(
            ["IT", "HR"]
        )
    ]
)


# ============================================================
# SECTION 56 - FILTER USING between()
# ============================================================

# between() checks whether values
# fall between two numbers.

print("\nSALARIES BETWEEN 50000 AND 65000:")

print(
    employees[
        employees["Salary"].between(
            50000,
            65000
        )
    ]
)


# ============================================================
# SECTION 57 - FILTER USING query()
# ============================================================

# query() allows us to write filtering conditions
# in a more readable way.

print("\nEMPLOYEES WITH SALARY ABOVE 55000:")

print(
    employees.query(
        "Salary > 55000"
    )
)


# ============================================================
# SECTION 58 - DATE AND TIME
# ============================================================

# Create example dates.

date_data = pd.DataFrame(
    {
        "Name": [
            "John",
            "Sarah",
            "Mike"
        ],

        "Start_Date": [
            "2026-01-15",
            "2026-02-20",
            "2026-03-05"
        ]
    }
)

print("\nORIGINAL DATE DATA:")
print(date_data)


# Convert the column from text
# into a real Pandas datetime column.

date_data["Start_Date"] = (
    pd.to_datetime(
        date_data["Start_Date"]
    )
)

print("\nCONVERTED DATE DATA:")
print(date_data)


# Extract the year.

date_data["Year"] = (
    date_data["Start_Date"].dt.year
)


# Extract the month.

date_data["Month"] = (
    date_data["Start_Date"].dt.month
)


# Extract the day.

date_data["Day"] = (
    date_data["Start_Date"].dt.day
)


# Extract the day name.

date_data["Day_Name"] = (
    date_data["Start_Date"]
    .dt.day_name()
)

print("\nDATE INFORMATION:")
print(date_data)


# ============================================================
# SECTION 59 - MERGE DATAFRAMES
# ============================================================

# Create employee information.

employee_info = pd.DataFrame(
    {
        "Employee_ID": [1, 2, 3],
        "Name": [
            "John",
            "Sarah",
            "Mike"
        ]
    }
)


# Create salary information.

salary_info = pd.DataFrame(
    {
        "Employee_ID": [1, 2, 3],
        "Salary": [
            50000,
            80000,
            70000
        ]
    }
)


# Merge the two DataFrames using Employee_ID.

merged_data = pd.merge(
    employee_info,
    salary_info,
    on="Employee_ID"
)

print("\nMERGED DATA:")
print(merged_data)


# ============================================================
# SECTION 60 - FINAL DATA ANALYSIS
# ============================================================

# Basic DataFrame shape.

print("\nDATASET SHAPE:")
print(employees.shape)


# Column names.

print("\nDATASET COLUMNS:")
print(employees.columns)


# Basic information about the DataFrame.

print("\nDATASET INFORMATION:")
employees.info()


# Statistical summary.

print("\nDATASET STATISTICS:")
print(
    employees.describe()
)


# Average salary.

average_salary = (
    employees["Salary"].mean()
)


# Highest salary.

highest_salary = (
    employees["Salary"].max()
)


# Lowest salary.

lowest_salary = (
    employees["Salary"].min()
)


# Total salary.

total_salary = (
    employees["Salary"].sum()
)


# Number of employees.

total_employees = len(employees)


# ============================================================
# FINAL EMPLOYEE REPORT
# ============================================================

print("\n")
print("==========================================")
print("       EMPLOYEE ANALYSIS REPORT")
print("==========================================")

print(
    f"Total Employees: {total_employees}"
)

print(
    f"Total Salary: ${total_salary:,.2f}"
)

print(
    f"Average Salary: ${average_salary:,.2f}"
)

print(
    f"Highest Salary: ${highest_salary:,.2f}"
)

print(
    f"Lowest Salary: ${lowest_salary:,.2f}"
)

print("==========================================")


# ============================================================
# END OF PANDAS BASICS PRACTICE
# ============================================================