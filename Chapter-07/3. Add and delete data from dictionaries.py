user_info = {
    'name': 'Waqar',
    'age': 20,
    'fav_movies': ['Dummy Movie 1', 'Dummy Movie 2', 'Dummy Movie 3'],
    'fav_tunes': ['Dummy Tune 1', 'Dummy Tune 2'],
}

# how to add data
user_info['fav_songs'] = ['Song1', 'Song2']
print(user_info)

# pop method - deletes a key:value pair from dictionary for provided key
popped_item = user_info.pop('fav_tunes')           # Removes and return its value
print(f'Popped item is {popped_item}')
print(user_info)

# popitem - deletes a key:value pair from dictionary randomly
popped_item_from_popitem = user_info.popitem()           # Removes key:value pair randomly and returns tuple of key:value pair
print(f'Popped item is {popped_item_from_popitem}')
print(type(popped_item_from_popitem))
print(user_info)
