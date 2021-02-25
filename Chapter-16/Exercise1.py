'''
Exercise#01: Create a laptop class with attributes like brand name, model name, price and create two objects/instance
of your laptop class
'''
class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name

laptop1 = Laptop('hp', 'au114tx', 63000)
laptop2 = Laptop('dell', 'Inspiron 15 3576', 50000)

print(laptop1.laptop_name)
print(laptop2.laptop_name)
print(f'Brand Name: {laptop1.brand_name}, Model Name: {laptop1.model_name}, Price: {laptop1.price}')
print(f'Brand Name: {laptop2.brand_name}, Model Name: {laptop2.model_name}, Price: {laptop2.price}')