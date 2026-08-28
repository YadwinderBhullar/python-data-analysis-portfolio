# Error Handling Practice
employees = {
    "John": 5000,
    "Sarah": 7000,
    "Mike": 4000,
    "David": 8000,
    "Lisa": 6500
}

name = input("Enter the employee's name: ")
def get_salary(employee_name):
    try:
        salary = employees[employee_name]
        return salary
    except KeyError:
        print(f"Employee '{employee_name}' not found.")
        return None
    except ValueError:
        print("Invalid input. Please enter a valid employee name.")
        return None
    except ZeroDivisionError:
        print("An unexpected error occurred.")
        return None
    
salary = get_salary(name)
print(salary)