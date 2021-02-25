# will discuss three problems in existing
# then we will solve them using getter, setter decorator

# class Phone:
#     def __init__(self, brand, model_name, price):
#         self.brand = brand
#         self.model_name = model_name
#         self._price = price
#         self.complete_specification = f'{self.brand} {self.model_name} and price is {self._price}'

#     def make_a_call(self, phone_number):
#         print(f'Calling {phone_number} ...')

#     def full_name(self):
#         return f'{self.brand} {self.model_name}'

# phone1 = Phone('Nokia', '1100', -1000)          # negative price first problem
# print(phone1.brand)
# print(phone1.model_name)
# print(phone1._price)
# phone1._price = 500                                       # price change krte wqt bhi negative de skty hain second problem
# print(phone1.complete_specification)           # price change krdi tb bhi is mein -1000 print hugi third problem

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)                 # little trick to solve this problem
        # if price>0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.complete_specification = f'{self.brand} {self.model_name} and price is {self._price}'

    @property                                   # ab isko as a function ni as a attribute ki trah call kr skte hain
    def complete_specification(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'

    @property
    def price(self):
        return self._price

    #property ke bad he setter bnana hai wrna problem hugi
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    def make_a_call(self, phone_number):
        print(f'Calling {phone_number} ...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

phone1 = Phone('Nokia', '1100', 1000)
print(phone1.price)
phone1.price = 1200
print(phone1.complete_specification)