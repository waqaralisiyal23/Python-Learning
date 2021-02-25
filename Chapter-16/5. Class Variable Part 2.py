# change class variable
# how to print name space for objects
# what if we use self instead of class name for class variables

class Laptop:
    percent_discount = 10

    def __init__(self, brand_name, model_name, price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name

    # instance method
    def apply_discount(self):
        return  self.price - ((self.price/100 ) * self.percent_discount)

laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('dell', 'Inspiron 15 3576', 50000)

Laptop.percent_discount = 20       # we can change class variable
print(f'Original Price: {laptop1.price}')
print(f'After Discount: {laptop1.apply_discount()}')

# We want to give 50% discount just for laptop2
laptop2.percent_discount = 50               # when we want specific value of class variable for our object
print(f'Original Price: {laptop2.price}')
print(f'After Discount: {laptop2.apply_discount()}')

# How to know that what things our object have
print(laptop1.__dict__)
print(laptop2.__dict__)