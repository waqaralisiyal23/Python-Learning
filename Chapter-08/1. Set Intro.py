# Set data type
# Unordered collection of unique data
# We cannot store tuples, lists and dictionaries in set but we can store numbers (including decimal) and strings

set_1 = {1, 2, 3, 2}
print(set_1)                    # {1, 2, 3}

list_1 = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8]
# remove duplicates from above list
list_2 = list(set(list_1))
print(list_2)

set_1.add(4)
print(set_1)                    # {1, 2, 3, 4}
set_1.add(5)
set_1.add(4)       # again add ni huga q ke already set mn hai
print(set_1)                    # {1, 2, 3, 4, 5}

set_1.remove(3)
print(set_1)
# set_1.remove(6)         # error because 6 is not present in set
set_1.discard(6)           # agr set mn value hugi tou remove hujyegi wrna kuch bhi ni huga error ni ayega

set_1_copy = set_1.copy()
print(set_1_copy)

set_1.clear()               # clears the set
print(set_1)

set_2 = {1, 1.1, 2.3, 'string'}
print(set_2)