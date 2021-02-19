# Why we use dictionaries?
# Ans: Because of limitation of lists, lists are not enough to represent real data.

# What are dictionaries?
# Ans: Unordered collection of data in key:value pair

# How to create dictionaries
user = {'name': 'Waqar', 'age': 20}
print(user)
print(type(user))

# Second method to create dictionary
user1 = {'name': 'Ahmed', 'age': 24}
print(user1)

# How to access data from dictionary
# Note: There is no indexing because of unordered collection of data
print(user['name'])
print(user['age'])

# Which type of data a dictionary can store
# anything
# numbers, strings, list, dictionary
user_info = {
    'name': 'Waqar',
    'age': 20,
    'fav_movies': ['Dummy Movie 1', 'Dummy Movie 2', 'Dummy Movie 3'],
    'fav_tunes': ['Dummy Tune 1', 'Dummy Tune 2'],
}
print(user_info['fav_movies'])

# How to add data to empty dictionary
user_info_2 = {}
user_info_2['name'] = 'Waqar'
print(user_info_2)

