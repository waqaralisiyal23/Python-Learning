# Class method as a constructor

class Person:
    count_instance = 0                  # class variable / class attribute

    def __init__(self, first_name, last_name, age):
        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        Person.count_instance +=1

    # class methods
    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(',')
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):
        return f'You have created {cls.count_instance} instances of {cls.__name__} class'

    # instance methods
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def is_above_18(self):
        return self.age > 18

person1 = Person('Waqar Ali', 'Siyal', 21)
person2 = Person('Ahmed Ali', 'Siyal', 24)
person3 = Person.from_string('Ahmed Ali,Keerio,18')

print(person3.full_name())
print(person3.age)