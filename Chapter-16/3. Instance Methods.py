# Instance methods

class Person:
    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # instance methods
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18

person1 = Person('Waqar Ali', 'Siyal', 21)
person2 = Person('Ahmed Ali', 'Siyal', 24)

print(person1.full_name())                              # Person.full_name(p1)       backgrond mn kis treeke se hu rha huta hai or hum ese bhi likh skte hain but likhngy ni
print(person2.full_name())

print(person1.is_above_18())
print(person2.is_above_18())
person3 = Person('Usama', 'Shaikh', 18)
print(person3.is_above_18())