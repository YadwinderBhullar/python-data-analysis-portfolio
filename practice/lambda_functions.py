# Lambda Functions Practice

# Python Lambda Practice

employees = {
    "John": 5000,
    "Sarah": 7000,
    "Mike": 4000,
    "David": 8000,
    "Lisa": 6500
}

# 1. Dasic lambda


double_salary = lambda salary: salary * 2
increase_salary = lambda salary: salary * 1.10

# 3. map() + zip()

names = list(employees.keys())
salaries = list(employees.values())

new_salaries = list(
    map(lambda salary: salary * 1.10, salaries)
)

print()
print("EMPLOYEE SALARY AFTER 10% INCREASE")
print("-----------------------------------")

for name, salary in zip(names, new_salaries):
    print(f"{name}: ${salary:,.2f}")

higher_salaries = list(
    filter(lambda salary: salary >= 6000, salaries)
)

print()
print("EMPLOYEES WITH SALARY >= $6000")
print()

# Test the lambda functions
print("DOUBLE SALARY")
print(double_salary(5000))

print()

print("10% SALARY INCREASE")
print(increase_salary(5000))
