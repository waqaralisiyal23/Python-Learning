'''
Exercise#02: Create same class as exercise1 and add a instance method apply_discount()
'''
class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance variables
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name+' '+model_name

    # instance method
    def apply_discount(self, percent_discount):
        return  self.price - ((self.price/100 ) * percent_discount)

laptop1 = Laptop('hp', 'au114tx', 63000)

print(f'Original Price: {laptop1.price}')
print(f'After Discount: {laptop1.apply_discount(10)}')