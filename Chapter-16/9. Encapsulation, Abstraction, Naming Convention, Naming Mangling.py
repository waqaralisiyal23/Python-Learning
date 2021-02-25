# Encapsulation
# Abstraction
# Some special naming convention
# Name mangling, __name (not a convention)

class Phone:
    def __init__(self, brand, model_name, price, price2):
        self.brand = brand
        self.model_name = model_name
        self._price = price
        self.__price = price2      # not needed instance variable just for understanding

    def make_a_call(self, phone_number):
        print(f'Calling {phone_number} ...')

    def full_name(self):
        return f'{self.brand} {self.model_name}'

    def send_message(self):
        '''
        suppose humne ye complete method bnaya hai or hum third party apis use krke ya kuch bhi krke message
        send kr rhy hain or jitna bhi hum code krein wo user se hide wo just is class ko use krke message send kre use ni pta
        hu ke iske andr complexity kitni hai ya kya logics hain tou ise he abstraction khty hain
        '''
        pass      # twilio

phone1 = Phone('Nokia', '1100', 1000, 1000)
print(phone1._price)
phone1._price = -1000    # We can change _price its public
print(phone1._price)

# print(phone1.__price)    # error
# Python ne khud __price isko change krke _Phone__price krdiya take ye isi class ka bna rhy baki zyada jab inheritance prhege smjh ayega
print(phone1.__dict__)
print(phone1._Phone__price)

# Some special naming convention
# _name   # convention of private name - ye public he huta hai srf developers ko btane ke liye huta hai ke iske sath ap cher char na krein
# __name__  # dunder/magic methods