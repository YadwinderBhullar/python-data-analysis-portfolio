class Employee:
    def __init__ (self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_info(self):
        print(self.name, "-",self.salary, "-", self.department)

    def give_raise(self, amount):
         self.salary = self.salary + amount


employee1 = Employee("John", 50000, "IT")
employee2 = Employee("Sarah", 60000 , "HR")
employee1.display_info()
employee2.display_info()
employee1.give_raise(5000)
employee1.display_info()
