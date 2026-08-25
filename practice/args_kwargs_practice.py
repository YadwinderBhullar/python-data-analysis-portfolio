# *args and **kwargs Practice


# ==========================================
# 1. *args
# ==========================================

def add_numbers(*numbers):
    return sum(numbers)


print("ADDING NUMBERS")
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40))


# ==========================================
# 2. **kwargs
# ==========================================

def employee_info(**details):

    for key, value in details.items():
        print(f"{key}: {value}")


print()
print("EMPLOYEE INFORMATION")

employee_info(
    name="John",
    salary=5000,
    department="Sales"
)


# ==========================================
# 3. *args + **kwargs
# ==========================================

def employee_data(*skills, **details):

    print()
    print("SKILLS")

    for skill in skills:
        print(skill)

    print()
    print("EMPLOYEE DETAILS")

    for key, value in details.items():
        print(f"{key}: {value}")


employee_data(
    "Python",
    "SQL",
    "Pandas",
    name="Sarah",
    salary=7000,
    department="Data Analysis"
)