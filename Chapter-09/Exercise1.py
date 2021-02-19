'''
Exercise#01: Define a function that take list of strings and returns a list which conains a reverse of every string
Note: USE LIST COMPREHENSION
'''
def reverse_strings_in_list(list_):
    return [item[::-1] for item in list_]
print(reverse_strings_in_list(['abc', 'def', 'ghi']))