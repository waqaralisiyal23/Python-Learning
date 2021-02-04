'''
Exercise#02: Define a function which will take list as a argument and returns a reversed list
Note: you can easily do this with reverse method or [ : :-1] but try to do this with the help of append and pop method
'''

def reverse_list(list):
    # First way
    # list.reverse()
    # return list

    # Second way
    # return list[ : :-1]

    # Third way
    reversed_list=[]
    for item in range(len(list)):
        reversed_list.append(list.pop())
    return reversed_list

print(reverse_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))