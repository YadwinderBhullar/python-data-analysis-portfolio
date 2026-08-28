
# write a code to read the file line by line and print each line
with open("practice/file-handling/employees.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()# Using strip() to remove any leading/trailing whitespace
print(line1)
print(line2)

#write a code to read all the lines fo the file and print each line
with open("practice/file-handling/employees.txt", "r") as file:
    employees = file.readlines()
    print(employees )
       # Using strip() to remove any leading/trailing whitespace

#write a code to read the file line by line and print each line using a for loop
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        print(line.strip())  # Using strip() to remove any leading/trailing whitespace

# write a code to read the file line by line and remove any leading/trailing whitespace and print only the employee names
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee_name = line.strip()
        employee = line.split(",")  # Using strip() to remove any leading/trailing whitespace
        print(employee[0])

# now lets print the employee name and salary separately by a colon
with open("practice/file-handling/employees.txt", "r") as file:
    for line in file:
        employee = line.strip().split(",")  # Using strip() to remove any leading/trailing whitespace
        print(f"Employee Name: {employee[0]} earns salary: {employee[1]}")