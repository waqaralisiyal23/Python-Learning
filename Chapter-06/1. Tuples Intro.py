# tuple data structure
# tuple can store any data type
# most important: tuples are immutable, once tuple is created you can't update
# no append, no insert, no pop, no remove
# tuples are faster than lists - thats why we use tuples when we don't want to change our data

example = ('one', 'two', 'three')
days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
# days[0] = 'changed value'     # error

# methods
# count -> to count how many times item present in tuple
# index -> to know about the index of particular element
# len -> To find the length of tuple

print(days.count('monday'))                    # 1
print(days.index('wednesday'))               # 2
print(len(days))                                       # 7
print(days[0:3])                                       # ('monday', 'tuesday', 'wednesday')     # tuple slicing


