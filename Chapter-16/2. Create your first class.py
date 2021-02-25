# Objectives
# What is class
# How to create an class
# What is init method, constructor
# What are attributes, Instance variables
# How to create our object

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

person1 = Person('Waqar Ali', 'Siyal', 21)
person2 = Person('Ahmed Ali', 'Siyal', 24)

print(person1.first_name, person1.last_name)
print(person1.age)
print(person2.first_name, person2.last_name)
print(person2.age)