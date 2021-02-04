# Data Structures
# Chapter#05: List
# Ordered collection of items
# You can store anything is Lists int, float, string

numbers = [1, 2, 3, 4, 5]
print(numbers[1])                    # prints the value at index 1 which is 2
print(numbers)

words = ['word1', 'word2', 'word3']
print(words[ :2])                       # prints the first two values
print(words)

mixed = [1, 2, 3, 4, 'five', 'six', 2.3, None]
print(mixed[-1])
print(mixed)

# you can change any value inside list
mixed[1] = 'two'
print(mixed[1])

mixed[1: ] = ['two', 'three']
print(mixed)
