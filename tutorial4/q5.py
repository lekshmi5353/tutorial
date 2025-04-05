class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")


person1 = Person("John", 30, 50000)
person2 = Person("Emily", 25, 45000)


person1.display()
person2.display()
