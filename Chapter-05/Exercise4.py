'''
Exercise#04: Define a function that will take list of numbers and filter odd and even numbers and returns a list
which contains two lists one for odd and one for even
input -----> [1,2,3,4,5,6,7,8,9,10]
output ----> [[,1,3,5,7,9], [2,4,6,8,10]]
'''

def filtered_even_odd_lists(list):
    odd_list = []
    even_list = []
    for num in list:
        if num%2==0:
            even_list.append(num)
        else:
            odd_list.append(num)
    return [odd_list, even_list]

print(filtered_even_odd_lists([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))