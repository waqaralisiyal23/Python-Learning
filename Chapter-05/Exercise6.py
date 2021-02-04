'''
Exercise#06: Define a function that take list as argument and returns the number of sublists present in that list
'''

def sublists_counter(my_list):
    count = 0
    for item in my_list:
        if type(item) == list:
            count+=1
    return count

print(sublists_counter([1, 2, [3,4], [5,6]]))