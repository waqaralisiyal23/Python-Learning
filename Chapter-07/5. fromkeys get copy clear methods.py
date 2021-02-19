# fromkeys
# d = {'name': 'unknown', 'age': 'unknown'}
d1 = dict.fromkeys(['name', 'age', 'height'], 'unknown')
print(d1)                  # {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

# You can also give tuple in place of list
d2 = dict.fromkeys(('name', 'age', 'height'), 'unknown')
print(d2)                  # {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

# What will happen if you use string ?
d3 = dict.fromkeys('abc', 'unknown')
print(d3)                  # {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

# Now try range function
# What will happen if you use string ?
d4 = dict.fromkeys(range(1, 6), 'unknown')
print(d4)                  # {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown'}


# get method (useful)
user = {'name': 'Waqar', 'age': 20}
# print(user['names']) # ab names koi key ni hai tou error ayega
print(user.get('names'))    # names nam ki koi key ni hai lekin error ni ayega None print huga so get() is better

if user.get('name'):
    print('present')
else:
    print('not present')
# if None:  -> this evaluates as False


# clear method - clears the dictionary
user.clear()
print(user)


# copy method
d1_copy = d1.copy()         # d1_copy and d1 are two different dictionaries stored at different location
print(d1_copy)

refer_d2 = d2             # both refering to the same dictionary - they both are same dictionaries means one dictionary in memory
print(refer_d2 is d2)   # is compares addresses so it will give True