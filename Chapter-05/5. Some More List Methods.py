# count
# sort method
# sorted function
# reverse
# clear
# copy
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']
print(fruits.count('apple'))                   # counts how many times apple present in list, output: 2

fruits.sort()                               # sorts the list
print(fruits)
numbers = [3, 5, 1, 9, 10]
numbers.sort()
print(numbers)

# if you don't want to sort the list just want to print in sorted order
numbers2 = [3, 5, 1, 9, 10]
print(sorted(numbers2))         # list will e printed in sorted order but remains same

numbers2.clear()                  # clears the list
print(numbers2)

fruits_copy = fruits.copy()
print(fruits_copy)

