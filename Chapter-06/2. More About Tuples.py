# Looping in tuples
# tuple with one element
# tuple without paranthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1, 2, 3, 4.0)

# for loop and tuple
for i in mixed:
    print(i)
# Note: You can use while loop too

# tuple with one element
# numbers = (1)           # this is not a tuple it is an integer
# words = ('word1')     # this is not a tuple it is an string
numbers = (1, )            # this is a tuple
words = ('word1', )      # this is a tuple

# tuple without paranthesis
guitars = 'yamaha', 'baton rouge', 'taylor'             # this is a tuple
print(type(guitars))                                    # <class 'tuple'>

# tuple unpacking
days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
day1, day2, day3, day4, day5, day6, day7 = (days)
print(day1, day2, day3, day4, day5, day6, day7)                                 # monday tuesday wednesday thursday friday saturday sunday

# list inside tuple
fruits = ('apple', ['orange', 'banana'])
# we can change list which is inside tuple
fruits[1].append('grapes')
print(fruits)                           # ('apple', ['orange', 'banana', 'grapes'])
del fruits[1][0]
print(fruits)                           # ('apple', ['banana', 'grapes'])

# Methods: min, max, sum
print(min(mixed))                       # 1
print(max(mixed))                      # 4.0
print(sum(mixed))                      # 10.0