numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# tuple to list
tuple_to_list = list(numbers)
print(tuple_to_list)                           # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(tuple_to_list))                 # <class 'list'>

# tuple to string
tuple_to_string = str(numbers)
print(tuple_to_string)                      # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   which is a string not a tuple
print(type(tuple_to_string))            # <class 'str'>

# list to string
list_to_string = str(tuple_to_list)
print(list_to_string)                      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   which is a string not a list
print(type(list_to_string))            # <class 'str'>