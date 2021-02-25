# Special magic/dunder methods
# operator overloading
# polymorphism - kisi cheez ki ek se zyada forms - one example is method overriding

class Phone:
    def __init__(self, brand, model, price):
        self.brand  = brand
        self.model = model
        self.price = price

    def phone_name(self):
        return f'{self.brand} {self.model}'

    # str, repr - ye tb call huty hain ja hum apne object ko print krte hain
    # developers str mn we formatted string return krte hain or repr mn object ki representation ko show krte hain
    def __str__(self):
        return f'{self.brand} {self.model}'

    def __repr__(self):
        return f'Phone(\'{self.brand}\', \'{self.model}\', {self.price})'

    # len - jab bhi len function ke andr humari class ka object pass krenge tou ye call huga
    def __len__(self):
        return len(self.phone_name())

    # operator overloading
    # add - ye tab call huga jab hum apni class ke do objects ko add krengy
    def __add__(self, other):
        return self.price + other.price

class SmartPhone(Phone):
    def __init__(self, brand, model, price, camera):
        super().__init__(brand, model, price)
        self.camera = camera

    def phone_name(self):
        return f'{self.brand} {self.model} and price is {self.price}'

my_phone = Phone('Nokia', '1100', 1000)
my_phone2 = Phone('Nokia', '1600', 1200)
# print(my_phone)
# agr dono __str__ or __repr__ define kiye hue hain tou str wala call huga lekin hum dono ko alg alg bhi call kr skte hain
print(str(my_phone))
print(repr(my_phone))
print(len(my_phone))

print(my_phone + my_phone2)

my_smartphone = SmartPhone('onePlus', '5t', 33000, '16 MP')
print(my_phone.phone_name())
print(my_smartphone.phone_name())
# Here phone_name() has more than one forms which is a example of polymorphism