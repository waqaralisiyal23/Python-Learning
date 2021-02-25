# Class Variable - same for each object

class Circle:
    pi = 3.14                               # class variable / class attribute

    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2*Circle.pi*self.radius

circle1 = Circle(4)
circle2 = Circle(5)

print(circle1.calculate_circumference())