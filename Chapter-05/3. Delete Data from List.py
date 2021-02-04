# pop method
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
fruits.pop()             # removes the last element and returns that element
print(fruits)
fruits.pop(1)          # removes the element at index 1 and returns that element
print(fruits)
# new fruits list = ['orange', 'pear', 'banana']

# del
# some people say this operator and some say this statement
del fruits[0]               # deletes the element at index 0
print(fruits)
# new fruits list = ['pear', 'banana']

# remove method
fruits.remove('banana')
print(fruits)