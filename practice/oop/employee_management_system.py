class Employee:
    def __init__(self, name, salary, department, performance):
        self.name = name
        self.salary = salary
        self.department = department
        self.performance = performance

    # Display employee information
    def display_info(self):
        print(
            self.name,
            "-",
            self.department,
            "- $",
            format(self.salary, ".2f"),
            "-",
            self.performance
        )

    # Give employee a raise
    def give_raise(self, amount):
        self.salary += amount

    # Calculate bonus based on performance
    def calculate_bonus(self):
        if self.performance == "Excellent":
            bonus = self.salary * 0.10
        elif self.performance == "Good":
            bonus = self.salary * 0.07
        elif self.performance == "Average":
            bonus = self.salary * 0.05
        else:
            bonus = 0

        return bonus

    # Calculate salary + bonus
    def get_total_compensation(self):
        bonus = self.calculate_bonus()
        total_compensation = self.salary + bonus
        return total_compensation


# --------------------------------------------------
# Functions for multiple employees
# --------------------------------------------------

def find_highest_compensation(employees):
    highest_compensation = 0
    highest_employee = None

    for employee in employees:
        total = employee.get_total_compensation()

        if total > highest_compensation:
            highest_compensation = total
            highest_employee = employee

    return highest_employee


def find_lowest_compensation(employees):
    lowest_compensation = employees[0].get_total_compensation()
    lowest_employee = employees[0]

    for employee in employees:
        total = employee.get_total_compensation()

        if total < lowest_compensation:
            lowest_compensation = total
            lowest_employee = employee

    return lowest_employee


# --------------------------------------------------
# Create employees
# --------------------------------------------------

employee1 = Employee("John", 50000, "IT", "Excellent")
employee2 = Employee("Sarah", 60000, "HR", "Good")
employee3 = Employee("Mike", 45000, "Sales", "Average")
employee4 = Employee("David", 40000, "IT", "Poor")

employees = [
    employee1,
    employee2,
    employee3,
    employee4
]


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

while True:

    print("\n===================================")
    print("     EMPLOYEE MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Display Employees")
    print("2. Give Raise")
    print("3. Show Bonus")
    print("4. Show Total Compensation")
    print("5. Find Highest Compensation")
    print("6. Find Lowest Compensation")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # ----------------------------------------------
    # Option 1 - Display Employees
    # ----------------------------------------------

    if choice == "1":

        print("\n--- Employees ---")

        for employee in employees:
            employee.display_info()

    # ----------------------------------------------
    # Option 2 - Give Raise
    # ----------------------------------------------

    elif choice == "2":

        print("\n--- Give Raise ---")

        new_employee = input("Enter employee name: ")

        try:
            employee_raise = float(
                input("Enter raise amount: ")
            )

            if employee_raise <= 0:
                print("Raise must be greater than 0.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        found = False

        for employee in employees:

            if new_employee.lower() == employee.name.lower():

                employee.give_raise(employee_raise)

                print(
                    employee.name,
                    "new salary: $",
                    format(employee.salary, ".2f")
                )

                found = True
                break

        if not found:
            print("Employee not found.")

    # ----------------------------------------------
    # Option 3 - Show Bonus
    # ----------------------------------------------

    elif choice == "3":

        print("\n--- Employee Bonuses ---")

        for employee in employees:

            bonus = employee.calculate_bonus()

            print(
                employee.name,
                "- Bonus: $",
                format(bonus, ".2f")
            )

    # ----------------------------------------------
    # Option 4 - Total Compensation
    # ----------------------------------------------

    elif choice == "4":

        print("\n--- Total Compensation ---")

        for employee in employees:

            total = employee.get_total_compensation()

            print(
                employee.name,
                "- Total: $",
                format(total, ".2f")
            )

    # ----------------------------------------------
    # Option 5 - Highest Compensation
    # ----------------------------------------------

    elif choice == "5":

        print("\n--- Highest Compensation ---")

        highest_employee = find_highest_compensation(employees)

        print("Employee:", highest_employee.name)

        print(
            "Salary: $",
            format(highest_employee.salary, ".2f")
        )

        print(
            "Bonus: $",
            format(highest_employee.calculate_bonus(), ".2f")
        )

        print(
            "Total Compensation: $",
            format(
                highest_employee.get_total_compensation(),
                ".2f"
            )
        )

    # ----------------------------------------------
    # Option 6 - Lowest Compensation
    # ----------------------------------------------

    elif choice == "6":

        print("\n--- Lowest Compensation ---")

        lowest_employee = find_lowest_compensation(employees)

        print("Employee:", lowest_employee.name)

        print(
            "Salary: $",
            format(lowest_employee.salary, ".2f")
        )

        print(
            "Bonus: $",
            format(lowest_employee.calculate_bonus(), ".2f")
        )

        print(
            "Total Compensation: $",
            format(
                lowest_employee.get_total_compensation(),
                ".2f"
            )
        )

    # ----------------------------------------------
    # Option 7 - Exit
    # ----------------------------------------------

    elif choice == "7":

        print("\nGoodbye! 👋")
        break

    # ----------------------------------------------
    # Invalid Choice
    # ----------------------------------------------

    else:

        print("\nInvalid choice. Please select 1-7.")