# raise errors example 1
# NotImplementedError
# abstract method

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define this method in subclasses')

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'Bhow Bhow'

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return 'Meow Meow'

dog1 = Dog('boony', 'pug')
print(dog1.sound())