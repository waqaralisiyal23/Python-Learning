# Can we derive more than one class from base class ?    Yes, we can
# Multilevel Inheritance
# Method Resolution Order
# Method Overriding
# isinstance(), issubclass()

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

    # overriden method
    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price}'

# We can derive more than one class from parent class
class SmartPhone2(Phone):                        # Derived class / Child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)          # first way - uncommon way
        super().__init__(brand, model_name, price)                   # second way - common way
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

# Multilevel inheritance - ek derived class bnaye phr usi derived class se ek or derived class bnayein
class FlagshipPhone(SmartPhone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera

    # overriden method
    def full_name(self):
        return f'{self.brand} {self.model_name} and price is {self._price} and front camera = {self.front_camera}'

# phone = Phone('nokia', '1100', 1000)
smart_phone = SmartPhone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
smart_phone2 = SmartPhone2('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
flagship_phone = FlagshipPhone('onePlus', '5t', 30000, '6 GB', '64 GB', '20 MP', '16 MP')

print(smart_phone2.full_name(), smart_phone2._price)
print(smart_phone.full_name())
print(flagship_phone.full_name())

# Method Resolution Order - mtlb python kis order mn classes ke andr attributes or methods ko search krta hai
# print(help(SmartPhone))
# print(help(FlagshipPhone))

# isinstance()
print(isinstance(smart_phone, SmartPhone))                   # True
print(isinstance(smart_phone, Phone))                            # True
print(isinstance(flagship_phone, Phone))                        # True
print(isinstance(smart_phone, FlagshipPhone))              # False

# issubclass()
print(issubclass(SmartPhone, Phone))                                 # True
print(issubclass(FlagshipPhone, Phone))                             # True
print(issubclass(SmartPhone, FlagshipPhone))                    # False
