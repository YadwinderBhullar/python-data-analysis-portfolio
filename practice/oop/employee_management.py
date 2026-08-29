class Employee:
    def __init__ (self, name, salary, department, performance):
        self.name = name
        self.salary = salary
        self.department  = department
        self.performance = performance

    def display_info(self):
       print(self.name, "-", self.salary , "-",self.department, "-", self.performance)
       print()

    def give_raise(self, amount):
        self.salary = self.salary + amount

    def calculate_bonus(self):
        if self.performance == "Excellent":
           bonus  = self.salary * 0.10
        elif self.performance =="Good":
            bonus = self.salary * 0.07
        elif self.performance == "Average":
            bonus = self.salary * 0.05
        else :
            bonus = 0
        return bonus
    
    def get_total_compensation(self):
        bonus = self.calculate_bonus()
        total_compensation = self.salary + bonus
        return total_compensation

def find_highest_compensation(employees):
    highest_employee  = None
    highest_compensation = 0
    for employee in employees:
       total = employee.get_total_compensation()
       if total > highest_compensation:
           highest_compensation = total
           highest_employee = employee.name
    return highest_employee

def find_lowest_compensation(employees):
    lowest_employee = None
    lowest_compensation = 999999
    for employee in employees:
        total= employee.get_total_compensation()
        if total < lowest_compensation:
            lowest_compensation = total
            lowest_employee = employee.name
    return lowest_employee


    
 
    

employee1 = Employee("John", 50000, "IT", "Excellent")
employee2 = Employee("Sarah", 60000, "HR", "Good")
employee3 = Employee("Mike", 45000, "Sales", "Average")
employee4 = Employee("David", 4000, "IT", "Poor")
employees = [employee1, employee2, employee3, employee4]
highest_employee = find_highest_compensation(employees)
lowest_employee = find_lowest_compensation(employees)
print("Highest Total Compensation:", highest_employee)
print("lowest Total Compensation:", lowest_employee)

employee1.display_info()
employee1.give_raise(5000)
employee1.display_info()



print(employee1.get_total_compensation())
print(employee2.get_total_compensation())
print(employee3.get_total_compensation())
print(employee4.get_total_compensation())


