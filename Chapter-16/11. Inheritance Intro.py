# Inheritance Intro

class Phone:                                                # Base class / Parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def make_a_call(self, phone_number):
        return f'Calling {phone_number} ...'

class SmartPhone(Phone):                        # Derived class / Child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)          # first way - uncommon way
        super().__init__(brand, model_name, price)                   # second way - common way
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

phone = Phone('nokia', '1100', 1000)
smart_phone = SmartPhone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')

print(phone.full_name())
print(smart_phone.full_name())
print(smart_phone._price)