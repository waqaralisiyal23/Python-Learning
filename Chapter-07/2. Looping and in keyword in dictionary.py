user_info = {
    'name': 'Waqar',
    'age': 20,
    'fav_movies': ['Dummy Movie 1', 'Dummy Movie 2', 'Dummy Movie 3'],
    'fav_tunes': ['Dummy Tune 1', 'Dummy Tune 2'],
}

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))

# keys method
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# items method
user_items = user_info.items()
print(user_items)
print(type(user_items))

# Check if key exist in dictionary
if 'name' in user_info:
    print('key exists')
else:
    print('key doesn\'t exists')

# Check if value exist in dictionary
if 20 in user_info.values():
    print('value exists')
else:
    print('value doesn\'t exists')

# Loops in dictionaries
# print all keys
for i in user_info:
    print(i, end=' ')
print()       # just for changing line
# print all values
for i in user_info.values():
    print(i, end=' ')
print()       # just for changing line
# print all values using keys
for i in user_info:
    print(user_info[i], end=' ')
print()       # just for changing line
# how items method is useful
for key, value in user_info.items():
    print(f'Key is {key} and Value is {value}')
# print all tuples
for i in user_info.items():
    print(i)