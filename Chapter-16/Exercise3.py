'''
Exercise#03: Create any class and count no. of objects created for that class
'''
class Person:
    count_instance = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        # Increment count_instance each time the object/instance is created
        Person.count_instance +=1

person1 = Person('Waqar Ali', 'Siyal', 21)
person2 = Person('Ahmed Ali', 'Siyal', 24)
person3 = Person('Usama', 'Shaikh', 20)
person4 = Person('Imtiaz', 'Buriro', 14)
person5 = Person('Uzair', 'Abro', 19)

print(f'No. of Objects: {Person.count_instance}')