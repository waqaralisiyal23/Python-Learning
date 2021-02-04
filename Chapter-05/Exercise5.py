'''
Exercise#05: Define a function which takes two lists as input and return a list which contains common elements
of both lists
'''

def common_elements(list1, list2):
    common_items = []
    for item in list1:
        if item in list2:
            common_items.append(item)
    return common_items

print(common_elements([1, 2, 3, 4, 5, 6], [5, 6, 7, 8, 9, 10]))