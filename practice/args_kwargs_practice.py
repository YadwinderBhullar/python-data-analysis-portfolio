# *args and **kwargs Practice


# 1. *args

def add_numbers(*numbers):
    return sum(numbers)


print("ADDING NUMBERS")
print(add_numbers(10, 20))
print(add_numbers(10, 20, 30))
print(add_numbers(10, 20, 30, 40))


# 2. **kwargs

def employee_info(**details):
    print(details)


print()
print("EMPLOYEE INFORMATION")

employee_info(
    name="John",
    salary=5000,
    department="Sales"
)