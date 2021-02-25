# raise errors example 2

class Mobile:
    def __init__(self, name):
        self.name = name

class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('New mobile should be object of Mobile class')

oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy s8'

mobile_store = MobileStore()
# mobile_store.add_mobile(samsung)       # TypeError
mobile_store.add_mobile(oneplus)
mobiles = mobile_store.mobiles
print(mobiles[0].name)