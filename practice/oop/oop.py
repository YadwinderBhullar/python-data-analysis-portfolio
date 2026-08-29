class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


student1 = Student("Yadwinder", 35, "A")
student2 = Student("John", 20, "B")
student3 = Student("James", 22,"C")
print(student1.name)
print(student1.age)
print(student1.grade)

print(student2.name)
print(student2.age)
print(student2.grade)

print(student3.name)
print(student3.age)
print(student3.grade)