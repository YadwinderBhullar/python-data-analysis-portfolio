class Employee:
    def __init__ (self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
employee1 =  Employee("John",22,20000)
employee2 =  Employee("James",22,6000)
employee3 =  Employee("Yad",22,112458)

print(employee1.salary)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
       print(self.brand, self.model, "-", self.year)

    def change_year(self, new_year):
        self.year = new_year

    def is_old(self):
        if self.year >=2020:
            print("This is a new car")
        else:
            print("This is an old car")
    
car1 = Car("Toyota"," Camry", 2022)
car2 = Car("Honda","Civic", 2020)
car1.is_old()
car2.is_old()
car1.change_year(2025)
car1.display_info()
car2.display_info()
