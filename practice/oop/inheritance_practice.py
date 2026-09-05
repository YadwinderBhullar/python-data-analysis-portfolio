class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


employee1 = Employee("John", 50000)
manager1 = Manager("Sarah", 80000, "Sales")

employee1.display_info()
print()

manager1.display_info()