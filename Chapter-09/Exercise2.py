'''
Exercise#02: Define a function which takes a list and list can contain any type of data it can have numbers, decimal numbers,
lists and dictionaries. You have to convert the numbers (including decimal) into string and store them in separate list
and return that list
'''
def num_to_string(list_):
    return [str(i) for i in list_ if (type(i)==int or type(i)==float)]
print(num_to_string([1, 'string1', 2, 3.0, 'string2', 4.5, [1, 2, 3], {'name': 'Waqar', 'age': 20}, 6.5]))
# ['1', '2', '3.0', '4.5', '6.5']