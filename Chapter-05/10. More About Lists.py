# generate list with range function
# index method

generated_list = list(range(1, 11))
print(generated_list)                              # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3]
print(numbers.index(3))          # gives the index of the provided element
print(numbers.index(3, 3))      # gives the index of the provided element and second argument is from which index to start searching
print(numbers.index(7, 4,  8))   # gives the index of the provided element, 2nd arg=start searching index & 3rd arg=stop searching



