# ============================================================
# PYTHON FILE HANDLING PRACTICE
# ============================================================


# ------------------------------------------------------------
# 1. Read the first two lines using readline()
# ------------------------------------------------------------

with open("practice/file-handling/employees.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()

print(line1)
print(line2)


# ------------------------------------------------------------
# 2. Read all lines using readlines()
# ------------------------------------------------------------

with open("practice/file-handling/employees.txt", "r") as file:
    employees = file.readlines()

print(employees)


# ------------------------------------------------------------
# 3. Read the file line by line using a for loop
# ------------------------------------------------------------

with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        print(line.strip())


# ------------------------------------------------------------
# 4. Read employee names only
# ------------------------------------------------------------

with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")
        print(employee[0])


# ------------------------------------------------------------
# 5. Read employee name and salary
# ------------------------------------------------------------

with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")

        print(
            f"Employee Name: {employee[0]} "
            f"earns salary: {employee[1]}"
        )


# ------------------------------------------------------------
# 6. Convert salary to integer and add $5,000
# ------------------------------------------------------------

with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")

        salary = int(employee[1])
        salary = salary + 5000

        print(
            f"Employee Name: {employee[0]} "
            f"earns salary: ${salary}"
        )


# ------------------------------------------------------------
# 7. Write data to a new file
# ------------------------------------------------------------

with open(
    "practice/file-handling/employees_backup.txt",
    "w"
) as file:
    file.write("David,55000\n")


# ------------------------------------------------------------
# 8. Create employees2.txt and write employee data
# ------------------------------------------------------------

with open(
    "practice/file-handling/employees2.txt",
    "w"
) as file:
    file.write("John,50000\n")
    file.write("Sarah,60000\n")
    file.write("Mike,45000\n")