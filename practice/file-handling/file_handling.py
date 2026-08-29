# ============================================================
# PYTHON FILE HANDLING + JSON PRACTICE
# ============================================================

import json


# ------------------------------------------------------------
# FILE HANDLING
# ------------------------------------------------------------

# Read first two lines
with open("practice/file-handling/employees.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)


# Read all lines
with open("practice/file-handling/employees.txt", "r") as file:
    employees = file.readlines()

print(employees)


# Read file line by line
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        print(line.strip())


# Read employee names
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")
        print(employee[0])


# Read employee name and salary
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")

        print(
            f"Employee Name: {employee[0]} "
            f"earns salary: ${employee[1]}"
        )


# Convert salary to integer and add $5,000
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")

        salary = int(employee[1])
        salary += 5000

        print(
            f"Employee Name: {employee[0]} "
            f"earns salary: ${salary}"
        )


# ------------------------------------------------------------
# JSON
# ------------------------------------------------------------

# Python dictionary
employee = {
    "name": "Sarah",
    "department": "Sales",
    "salary": 60000
}


# Python dictionary → JSON file
with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)


# JSON file → Python dictionary
with open("employee.json", "r") as file:
    employee = json.load(file)

print(employee)

import math

number = 64

print(math.sqrt(number))