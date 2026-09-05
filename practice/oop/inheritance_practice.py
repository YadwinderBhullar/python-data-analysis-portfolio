class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.10
        



class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.20


class Developer(Employee):
    def __init__(self, name , salary, programming_language):
        super().__init__(name,salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.15




employee1 = Employee("John", 50000)
manager1 = Manager("Sarah", 80000, "Sales")
developer1 = Developer("Mike",70000, "python")





employees = [employee1, manager1, developer1]
for employee in employees:
    employee.display_info()
    print(f"Bonus: ${employee.calculate_bonus()}")
    print()





